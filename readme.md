# VideoMentor AI

## Overview

VideoMentor AI is an AI-powered learning assistant that converts educational videos into easy-to-understand study materials.

Users can upload local video files or provide YouTube URLs. The platform automatically extracts speech, generates transcripts, translates content into the user's preferred language, creates concise study notes, and generates interactive quizzes.

The goal is to make learning from video content faster, more accessible, and language-independent.

---

## Features

### Video Input

* Upload local video files
* Process YouTube video URLs
* Support for educational lectures and tutorials

### Speech-to-Text

* Automatic transcript generation
* Multi-language speech recognition using Whisper

### Translation

* Translate transcripts into multiple languages
* Support for English, Malayalam, Hindi, Tamil, Arabic, and more

### AI Study Assistant

* Generate concise summaries
* Extract key learning points
* Create topic-wise study notes

### Quiz Generation

* Multiple-choice questions (MCQs)
* True/False questions
* Short-answer questions

### Future Enhancements

* PDF export
* Transcript search
* AI chatbot for video content
* Flashcard generation
* Learning progress tracking

---

## System Workflow

Video Upload / YouTube URL
↓
Audio Extraction
↓
Speech-to-Text (Whisper)
↓
Transcript Generation
↓
Translation
↓
Summary & Notes Generation
↓
Quiz Generation

---

## Technology Stack

### Frontend

* Streamlit

### AI & NLP

* Whisper
* Hugging Face Transformers
* MarianMT / NLLB
* Groq API (for notes and quiz generation)

### Media Processing

* FFmpeg
* yt-dlp

### Programming Language

* Python

---

## Project Structure

VideoMentorAI/

├── app.py

├── uploads/

├── outputs/

├── utils/

│   ├── audio_extractor.py

│   ├── transcriber.py

│   ├── translator.py

│   ├── notes_generator.py

│   ├── quiz_generator.py

│   └── youtube_processor.py

├── requirements.txt

├── README.md

└── .env

---

## Installation

### Clone the Repository

git clone <repository-url>

cd VideoMentorAI

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### Run the Application

streamlit run app.py

---

## Development Roadmap

### Phase 1

* Streamlit interface
* Video upload
* Language selection

### Phase 2

* Audio extraction using FFmpeg

### Phase 3

* Transcript generation using Whisper

### Phase 4

* Transcript translation

### Phase 5

* Notes generation

### Phase 6

* Quiz generation

### Phase 7

* YouTube URL support

### Phase 8

* Long-video processing and optimization

---

## Target Users

* Students
* Educators
* Online learners
* Content creators
* Training organizations

---

## License

This project is intended for educational, research, and personal development purposes.

---

## Author

**Nandhana M J**

VideoMentor AI