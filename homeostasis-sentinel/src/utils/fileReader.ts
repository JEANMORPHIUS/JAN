import { parseMarkdownContent, ParsedMarkdown } from './markdownParser';

/** * * Read markdown files from a directory using File System Access API
 *  * Falls back to file input if API is not available
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
export async function readMarkdownFilesFromDirectory(): Promise<ParsedMarkdown[]> {
  try {
    // Try File System Access API (Chrome/Edge)
    if ('showDirectoryPicker' in window) {
      return await readFilesWithDirectoryPicker();
    } else {
      throw new Error('File System Access API not supported. Use file input instead.');
    }
  } catch (error) {
    console.error('Error reading directory:', error);
    throw error;
  }
}

async function readFilesWithDirectoryPicker(): Promise<ParsedMarkdown[]> {
  const dirHandle = await (window as any).showDirectoryPicker();
  const files: ParsedMarkdown[] = [];
  
  for await (const entry of dirHandle.values()) {
    if (entry.kind === 'file' && entry.name.endsWith('.md')) {
      const file = await entry.getFile();
      const content = await file.text();
      files.push(parseMarkdownContent(content, entry.name));
    }
  }
  
  return files;
}

/**
 * Read markdown files from FileList (file input)
 */
export async function readMarkdownFilesFromInput(fileList: FileList): Promise<ParsedMarkdown[]> {
  const files: ParsedMarkdown[] = [];
  
  for (let i = 0; i < fileList.length; i++) {
    const file = fileList[i];
    if (file.name.endsWith('.md')) {
      const content = await file.text();
      files.push(parseMarkdownContent(content, file.name));
    }
  }
  
  return files;
}

