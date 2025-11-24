from database.models import SessionLocal, Candidate, Skill, Education, Experience

def view_database():
    db = SessionLocal()
    try:
        print("=== CANDIDATES ===")
        candidates = db.query(Candidate).all()
        for candidate in candidates:
            print(f"ID: {candidate.id}, Name: {candidate.name}, Email: {candidate.email}")
            print(f"Skills: {[skill.name for skill in candidate.skills]}")
            print("---")
        
        print("\n=== SKILLS ===")
        skills = db.query(Skill).all()
        for skill in skills:
            print(f"ID: {skill.id}, Name: {skill.name}, Category: {skill.category}")
        
        print(f"\nTotal Candidates: {len(candidates)}")
        print(f"Total Skills: {len(skills)}")
        
    finally:
        db.close()

if __name__ == "__main__":
    view_database()