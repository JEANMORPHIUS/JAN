/** * * DAY 3: FIRST FRUITS ANOINTING
 *  * Morning Giving Tracker, Afternoon Faith-Based Decision Logger
 *  * 
 *  * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 *  * Spiritual Alignment Over Mechanical Productivity
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * THE MISSION:
 * THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 * LOVE IS THE HIGHEST MASTERY
 * ENERGY + LOVE = WE ALL WIN
 * PEACE, LOVE, UNITY
 * 
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import { useState, useEffect } from 'react';
import { GivingAct, FaithDecision } from '../../types/divineTiming';
import styles from './Day3Activation.module.css';

interface Day3ActivationProps {
  onComplete: (data: {
    givingActs: GivingAct[];
    faithDecisions: FaithDecision[];
  }) => void;
}

export default function Day3Activation({ onComplete }: Day3ActivationProps) {
  const [givingActs, setGivingActs] = useState<GivingAct[]>([]);
  const [faithDecisions, setFaithDecisions] = useState<FaithDecision[]>([]);
  
  const [newGiving, setNewGiving] = useState({
    description: '',
    amount: '',
    recipient: '',
    faithLevel: 5
  });
  
  const [newDecision, setNewDecision] = useState({
    decision: '',
    context: '',
    outcome: ''
  });

  const addGivingAct = () => {
    if (newGiving.description.trim() && newGiving.recipient.trim()) {
      const act: GivingAct = {
        id: Date.now().toString(),
        description: newGiving.description,
        amount: newGiving.amount ? Number(newGiving.amount) : undefined,
        recipient: newGiving.recipient,
        timestamp: new Date(),
        faithLevel: newGiving.faithLevel
      };
      setGivingActs(prev => [...prev, act]);
      setNewGiving({
        description: '',
        amount: '',
        recipient: '',
        faithLevel: 5
      });
    }
  };

  const addFaithDecision = () => {
    if (newDecision.decision.trim() && newDecision.context.trim()) {
      const decision: FaithDecision = {
        id: Date.now().toString(),
        decision: newDecision.decision,
        context: newDecision.context,
        timestamp: new Date(),
        outcome: newDecision.outcome || undefined
      };
      setFaithDecisions(prev => [...prev, decision]);
      setNewDecision({
        decision: '',
        context: '',
        outcome: ''
      });
    }
  };

  useEffect(() => {
    if (givingActs.length > 0 && faithDecisions.length > 0) {
      onComplete({
        givingActs,
        faithDecisions
      });
    }
  }, [givingActs, faithDecisions, onComplete]);

  return (
    <div className={styles.day3Container}>
      <div className={styles.dayHeader}>
        <div className={styles.dayNumber}>DAY 3</div>
        <div className={styles.dayTitle}>First Fruits Anointing</div>
      </div>

      {/* Morning Giving Tracker */}
      <div className={styles.section}>
        <div className={styles.sectionTitle}>Morning Acts of Faith</div>
        <div className={styles.sectionSubtitle}>Track your giving acts</div>

        <div className={styles.givingForm}>
          <div className={styles.formGroup}>
            <label>Description of Giving Act:</label>
            <textarea
              value={newGiving.description}
              onChange={(e) => setNewGiving(prev => ({ ...prev, description: e.target.value }))}
              placeholder="What did you give? (time, money, resources, etc.)"
              className={styles.textInput}
              rows={3}
            />
          </div>

          <div className={styles.formRow}>
            <div className={styles.formGroup}>
              <label>Recipient:</label>
              <input
                type="text"
                value={newGiving.recipient}
                onChange={(e) => setNewGiving(prev => ({ ...prev, recipient: e.target.value }))}
                placeholder="Who received this?"
                className={styles.textInput}
              />
            </div>

            <div className={styles.formGroup}>
              <label>Amount (optional):</label>
              <input
                type="number"
                value={newGiving.amount}
                onChange={(e) => setNewGiving(prev => ({ ...prev, amount: e.target.value }))}
                placeholder="Amount"
                className={styles.numberInput}
              />
            </div>
          </div>

          <div className={styles.faithLevelGroup}>
            <label>Faith Level: {newGiving.faithLevel}</label>
            <input
              type="range"
              min="1"
              max="10"
              value={newGiving.faithLevel}
              onChange={(e) => setNewGiving(prev => ({ ...prev, faithLevel: Number(e.target.value) }))}
              className={styles.slider}
            />
            <div className={styles.sliderLabels}>
              <span>Low</span>
              <span>High</span>
            </div>
          </div>

          <button
            onClick={addGivingAct}
            disabled={!newGiving.description.trim() || !newGiving.recipient.trim()}
            className={styles.addButton}
          >
            Add Giving Act
          </button>
        </div>

        <div className={styles.actsList}>
          <div className={styles.listTitle}>Giving Acts Logged: {givingActs.length}</div>
          {givingActs.map((act) => (
            <div key={act.id} className={styles.actItem}>
              <div className={styles.actDescription}>{act.description}</div>
              <div className={styles.actMeta}>
                <span>To: {act.recipient}</span>
                {act.amount && <span>Amount: {act.amount}</span>}
                <span>Faith: {act.faithLevel}/10</span>
                <span className={styles.actTime}>
                  {new Date(act.timestamp).toLocaleTimeString()}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Afternoon Faith-Based Decision Logger */}
      <div className={styles.section}>
        <div className={styles.sectionTitle}>Afternoon Faith-Based Decisions</div>
        <div className={styles.sectionSubtitle}>Log decisions made in faith</div>

        <div className={styles.decisionForm}>
          <div className={styles.formGroup}>
            <label>Decision Made:</label>
            <textarea
              value={newDecision.decision}
              onChange={(e) => setNewDecision(prev => ({ ...prev, decision: e.target.value }))}
              placeholder="What decision did you make in faith?"
              className={styles.textInput}
              rows={2}
            />
          </div>

          <div className={styles.formGroup}>
            <label>Context:</label>
            <textarea
              value={newDecision.context}
              onChange={(e) => setNewDecision(prev => ({ ...prev, context: e.target.value }))}
              placeholder="What was the situation or context?"
              className={styles.textInput}
              rows={3}
            />
          </div>

          <div className={styles.formGroup}>
            <label>Outcome (optional - can add later):</label>
            <textarea
              value={newDecision.outcome}
              onChange={(e) => setNewDecision(prev => ({ ...prev, outcome: e.target.value }))}
              placeholder="What was the outcome? (if known)"
              className={styles.textInput}
              rows={2}
            />
          </div>

          <button
            onClick={addFaithDecision}
            disabled={!newDecision.decision.trim() || !newDecision.context.trim()}
            className={styles.addButton}
          >
            Log Faith Decision
          </button>
        </div>

        <div className={styles.decisionsList}>
          <div className={styles.listTitle}>Faith Decisions Logged: {faithDecisions.length}</div>
          {faithDecisions.map((decision) => (
            <div key={decision.id} className={styles.decisionItem}>
              <div className={styles.decisionText}>{decision.decision}</div>
              <div className={styles.decisionContext}>Context: {decision.context}</div>
              {decision.outcome && (
                <div className={styles.decisionOutcome}>Outcome: {decision.outcome}</div>
              )}
              <div className={styles.decisionTime}>
                {new Date(decision.timestamp).toLocaleTimeString()}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
