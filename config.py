import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/resume_parser")
    
    # Groq API Configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")  # Updated to working model
    
    # File Upload
    MAX_FILE_SIZE = 10 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'.pdf', '.docx', '.doc', '.txt', '.png', '.jpg', '.jpeg'}
    
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

settings = Settings()