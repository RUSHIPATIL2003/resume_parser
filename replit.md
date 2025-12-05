# AI Resume Screening System - Replit Setup

## Overview
An intelligent resume parsing and screening system built with FastAPI and Groq's ultra-fast LLM API. This application automatically extracts structured information from resumes in multiple formats and provides AI-powered skill-based candidate search with job role matching.

## Current Status
✅ Successfully configured and running in Replit environment
- FastAPI application running on port 5000
- PostgreSQL database (Replit-managed)
- Groq API integrated for AI-powered resume parsing
- Tesseract OCR for image-based resume processing

## Tech Stack
- **Backend**: FastAPI (Python 3.11)
- **Database**: PostgreSQL (Replit-managed)
- **AI/LLM**: Groq API (llama-3.3-70b-versatile)
- **OCR**: Tesseract
- **Frontend**: Vanilla JavaScript, HTML5, CSS3

## Environment Variables
The following environment variables are configured:
- `GROQ_API_KEY` (Secret): Your Groq API key for resume parsing
- `GROQ_MODEL`: llama-3.3-70b-versatile
- `DEBUG`: True
- `DATABASE_URL`: Auto-managed by Replit (PostgreSQL)

## Features
1. **Multi-format Resume Support**: PDF, DOCX, DOC, TXT, PNG, JPG, JPEG
2. **AI-Powered Entity Extraction**: Uses Groq's Llama 3.3 70B model
3. **Smart Skill-Based Search**: Fuzzy matching with synonym support
4. **70% Minimum Match Filter**: Only displays candidates with ≥70% skill match
5. **Job Role Matching**: 10 pre-built job roles with percentage-based ranking
6. **Resume Document Viewer**: View parsed resumes directly in browser
7. **Extracted Information Display**: Name, skills, education, experience, location

## Project Structure
```
├── app.py                          # Main FastAPI application
├── config.py                       # Configuration and settings
├── requirements.txt                # Python dependencies
├── database/
│   ├── models.py                   # SQLAlchemy models
│   ├── shortlist_sqlite.py         # Shortlist database management
├── services/
│   ├── file_processor.py           # PDF/DOCX/Image parsing
│   ├── groq_parser.py              # Groq API integration
│   ├── llm_parser.py               # LLM parsing orchestration
│   ├── search_engine.py            # Candidate search & job role matching
│   ├── shortlisted_db.py           # Shortlisted candidates database
├── static/
│   ├── script.js                   # Frontend JavaScript
│   ├── style.css                   # Frontend styling
├── templates/
│   └── index.html                  # Main web interface
├── utils/
│   ├── helpers.py                  # Utility functions
│   └── validation.py               # Input validation
└── uploads/                        # Resume file storage (auto-created)
```

## How to Use
1. **Upload Resumes**: Drag and drop or browse for files (PDF, DOCX, DOC, TXT, PNG, JPG, JPEG)
2. **Search by Skills**: Enter skills like "Python", "React.js", "AWS" to find matching candidates
3. **Search by Job Role**: Search for roles like "MERN Stack Developer", "Data Scientist", etc.
4. **View Candidate Details**: Select a resume from dropdown to view details and extracted information
5. **Download Resume Files**: Access original resume files for verification

## Available Job Roles
The system includes 10 pre-built job roles:
1. MERN Stack Developer
2. Full Stack Developer
3. Frontend Developer
4. Backend Developer
5. Data Scientist
6. DevOps Engineer
7. Mobile Developer
8. UI/UX Designer
9. Cloud Architect
10. QA Engineer

## API Endpoints
- `GET /` - Main web interface
- `POST /api/upload-resume` - Upload and parse resume
- `GET /api/resumes` - List all candidates
- `GET /api/resume/{candidate_id}` - Get candidate details
- `GET /api/resume/file/{candidate_id}` - Download resume file
- `GET /api/search?q=<skill>` - Search by skill (filters ≥70% match, only NEW candidates)
- `GET /api/search-by-role?role=<role_name>` - Search by job role (only NEW candidates)
- `GET /api/job-roles` - Get all available job roles
- `GET /api/shortlisted` - Get shortlisted candidates
- `DELETE /api/shortlisted` - Clear all shortlisted candidates
- `POST /api/reset-search-status` - Reset all candidates to unsearched (re-search all resumes)
- `GET /api/search-stats` - Get statistics about searched vs unsearched candidates

## Database Schema
- **candidates**: Stores candidate information (name, email, phone, location, etc.)
- **skills**: Normalized skills with categories
- **education**: Educational background
- **experiences**: Work experience records
- **candidate_skills**: Many-to-many relationship between candidates and skills

## Development Notes
- The application uses PostgreSQL database managed by Replit
- Database tables are automatically created on startup via SQLAlchemy
- Uploads directory stores resume files
- The application runs on port 5000 with host 0.0.0.0
- Cache control is enabled to prevent caching issues in the Replit webview

## Deployment
The application is configured for Replit deployment with autoscale deployment target:
- **Type**: Autoscale (stateless web application)
- **Run Command**: `uvicorn app:app --host 0.0.0.0 --port ${PORT:-5000}`
- **Database**: Uses Replit-managed PostgreSQL (DATABASE_URL is automatically set)
- The deployment automatically manages scaling based on traffic
- Port is dynamically assigned via $PORT environment variable in production

## Troubleshooting
- If uploads fail, ensure the `uploads/` directory exists
- If database errors occur, check PostgreSQL connection
- If OCR fails, verify Tesseract installation
- If Groq API fails, verify GROQ_API_KEY is set correctly

## Recent Changes
- 2025-12-05: Smart Search Filtering Feature Added
  - Search now only processes NEW (unsearched) candidates to avoid re-processing existing ones
  - Shortlisted candidates table is cleared before each new search
  - Added `is_searched` field to track processed candidates
  - Added API endpoint to reset search status if you want to re-search all candidates
  - Added API endpoint to view search statistics (total, searched, unsearched counts)

- 2025-12-05: Initial Replit setup completed
  - Installed Python 3.11 and all dependencies
  - Configured Tesseract for OCR support
  - Set up environment variables (GROQ_API_KEY, GROQ_MODEL, DEBUG)
  - Configured workflow to run on port 5000
  - Configured deployment settings for production
  - Application successfully running and serving requests
