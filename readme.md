# AI Resume Screening with Groq API

An intelligent resume parsing system that extracts entities from resumes using Groq's ultra-fast LLMs and provides skill-based search functionality.

## Features

-  **Multi-format Support**: PDF, DOCX, DOC, TXT, Images (PNG, JPG)
-  **AI-Powered Parsing**: Uses Groq's Mixtral/Llama2 models
-  **Smart Search**: Skill-based candidate matching with percentages
-  **PostgreSQL Storage**: Structured data storage
-  **Web Interface**: Easy-to-use web dashboard
-  **High Performance**: Groq API provides 200-300 tokens/second

## Quick Start

### 1. Get Groq API Key
```bash
# Visit https://console.groq.com/ and get your free API key
# Free tier: 5,000 requests/day


2. Setup Environment

# Clone and setup
git clone <your-repo>
cd resume_parser

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env and add your Groq API key

3. Setup PostgreSQL

# Install PostgreSQL (if not already installed)
# Then run:
python setup_database.py


4. Run Application

python app.py

Visit: http://localhost:8000

