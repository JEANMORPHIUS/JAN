#!/usr/bin/env python3
'''
Scripture Education Flask App
Serves 376 lessons offline on Raspberry Pi

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Purpose Not Performance
'''

from flask import Flask, render_template, jsonify, send_from_directory
import json
from pathlib import Path

app = Flask(__name__)

# Configuration
LESSONS_DIR = Path('../lessons')
AUDIO_DIR = Path('../audio')
IMAGES_DIR = Path('../images')

@app.route('/')
def index():
    '''Home page'''
    return render_template('index.html')

@app.route('/api/lessons')
def get_lessons():
    '''Get all lessons'''
    lessons = []
    for lesson_file in LESSONS_DIR.glob('*.json'):
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lessons.append(json.load(f))
    return jsonify(lessons)

@app.route('/api/lessons/<lesson_id>')
def get_lesson(lesson_id):
    '''Get specific lesson'''
    lesson_file = LESSONS_DIR / f'{lesson_id}.json'
    if lesson_file.exists():
        with open(lesson_file, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify({'error': 'Lesson not found'}), 404

@app.route('/audio/<filename>')
def serve_audio(filename):
    '''Serve audio files'''
    return send_from_directory(AUDIO_DIR, filename)

@app.route('/images/<filename>')
def serve_image(filename):
    '''Serve image files'''
    return send_from_directory(IMAGES_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
