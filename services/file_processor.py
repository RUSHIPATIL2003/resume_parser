import os
import pdfplumber
from docx import Document
import pytesseract
from PIL import Image
import io
import re
from typing import Optional

class FileProcessor:
    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        """Extract text from PDF files"""
        text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
        return text

    @staticmethod
    def extract_text_from_docx(file_path: str) -> str:
        """Extract text from DOCX files"""
        try:
            doc = Document(file_path)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            return text
        except Exception as e:
            raise Exception(f"Error reading DOCX: {str(e)}")

    @staticmethod
    def extract_text_from_image(file_path: str) -> str:
        """Extract text from image files using OCR"""
        try:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            raise Exception(f"Error processing image: {str(e)}")

    @staticmethod
    def extract_text_from_file(file_path: str, file_extension: str) -> str:
        """Main method to extract text from any supported file type"""
        if file_extension.lower() in ['.pdf']:
            return FileProcessor.extract_text_from_pdf(file_path)
        elif file_extension.lower() in ['.docx', '.doc']:
            return FileProcessor.extract_text_from_docx(file_path)
        elif file_extension.lower() in ['.png', '.jpg', '.jpeg']:
            return FileProcessor.extract_text_from_image(file_path)
        elif file_extension.lower() in ['.txt']:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        else:
            raise Exception(f"Unsupported file format: {file_extension}")

    @staticmethod
    def clean_extracted_text(text: str) -> str:
        """Clean and preprocess extracted text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^\w\s.,!?;:()\-]', '', text)
        return text.strip()