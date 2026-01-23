import React from 'react';
import { HealthMetrics } from '../types';
import { extractTagsFromContent, getPriorityTags } from '../utils/dataProcessor';
import { processHealthData } from '../utils/dataProcessor';
import { ParsedMarkdown } from '../types';

interface ProjectJournalProps {
  metrics: HealthMetrics[];
  parsedFiles?: ParsedMarkdown[];
}

export const ProjectJournal: React.FC<ProjectJournalProps> = ({ metrics, parsedFiles }) => {
  // Combine metrics with tags from parsed files if available
  const entriesWithNotes = metrics
    .filter(m => m.mental_emotional_sway && m.mental_emotional_sway.trim().length > 0)
    .map(metric => {
      // Try to find matching parsed file to extract tags
      const matchingFile = parsedFiles?.find(f => {
        const fileDate = f.filename.match(/(\d{4}-\d{2}-\d{2})/)?.[1];
        return fileDate === metric.date;
      });

      const content = matchingFile?.content || metric.mental_emotional_sway || '';
      const allTags = extractTagsFromContent(content);
      const priorityTags = getPriorityTags(allTags);

      return {
        ...metric,
        allTags,
        priorityTags
      };
    })
    .sort((a, b) => b.date!.localeCompare(a.date!));

  return (
    <div className="project-journal">
      <h3 className="section-title">Project Journal: Mental/Emotional Sway</h3>
      <div className="journal-entries">
        {entriesWithNotes.length > 0 ? (
          entriesWithNotes.map((metric, idx) => (
            <div key={idx} className="journal-entry">
              <div className="journal-header">
                <div className="journal-date">
                  {new Date(metric.date!).toLocaleDateString('en-US', {
                    weekday: 'long',
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric'
                  })}
                </div>
                <div className="journal-metrics">
                  {metric.vision_clarity !== undefined && (
                    <span className="metric-badge">
                      Vision: {metric.vision_clarity}/10
                    </span>
                  )}
                  {metric.muscle_tension !== undefined && (
                    <span className="metric-badge">
                      Tension: {metric.muscle_tension}/10
                    </span>
                  )}
                </div>
              </div>
              {'priorityTags' in metric && metric.priorityTags.length > 0 && (
                <div className="journal-priority-tags">
                  {metric.priorityTags.map((tag, tagIdx) => (
                    <span key={tagIdx} className={`priority-tag tag-${tag}`}>
                      #{tag}
                    </span>
                  ))}
                </div>
              )}
              {'allTags' in metric && metric.allTags.length > 0 && metric.allTags.length > (metric.priorityTags?.length || 0) && (
                <div className="journal-tags">
                  {metric.allTags.filter(tag => !metric.priorityTags?.includes(tag)).map((tag, tagIdx) => (
                    <span key={tagIdx} className="journal-tag">
                      #{tag}
                    </span>
                  ))}
                </div>
              )}
              <div className="journal-content">
                {metric.mental_emotional_sway!.split('\n').map((line, lineIdx) => (
                  <p key={lineIdx} className="journal-text">
                    {line}
                  </p>
                ))}
              </div>
            </div>
          ))
        ) : (
          <div className="no-data-message">
            No journal entries found. Add "Mental/Emotional Sway" notes to your markdown files.
          </div>
        )}
      </div>
    </div>
  );
};

