from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

def list_available_models():
    """List all currently available Groq models"""
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        print(" GROQ_API_KEY not found in .env file")
        return
    
    try:
        client = Groq(api_key=api_key)
        models = client.models.list()
        
        print(" CURRENTLY AVAILABLE GROQ MODELS:")
        print("=" * 50)
        
        available_models = []
        for model in models.data:
            print(f" {model.id}")
            available_models.append(model.id)
        
        print("\n Recommended for resume parsing:")
        # Look for models with '70b' or large context
        for model in available_models:
            if '70b' in model.lower() or '8x7b' in model.lower() or '8x22b' in model.lower():
                print(f"    {model}")
        
        return available_models
        
    except Exception as e:
        print(f" Error: {e}")
        return []

if __name__ == "__main__":
    list_available_models()