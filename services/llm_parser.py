from .groq_parser import GroqResumeParser
from typing import Dict, Any, List

class LLMResumeParser:
    def __init__(self):
        self.parser = GroqResumeParser()
    
    def parse_resume(self, text: str) -> Dict[str, Any]:
        """Main method to parse resume text using Groq"""
        return self.parser.parse_resume(text)
    
    def extract_skills_with_llm(self, text: str) -> List[str]:
        """Extract skills using Groq"""
        try:
            prompt = f"""
            Extract ONLY technical skills, programming languages, tools, and frameworks from this resume text.
            Be comprehensive - include all technologies mentioned anywhere in the text.
            Return as a JSON array: ["skill1", "skill2", ...]
            
            Resume Text:
            {text[:4000]}
            """
            
            response = self.parser.client.chat.completions.create(
                model=self.parser.model,
                messages=[
                    {"role": "system", "content": "You extract technical skills from resumes. Return only JSON arrays."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=1000
            )
            
            result_text = response.choices[0].message.content
            import json
            skills = json.loads(result_text)
            return skills if isinstance(skills, list) else []
            
        except Exception as e:
            print(f"Skill extraction failed: {e}")
            return self.parser._get_common_skills()