from database.models import Base, engine
import sys

def setup_database():
    """Create all database tables"""
    print(" Setting up database tables...")
    
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print(" Database tables created successfully")
        
        # Verify tables were created
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        print(" Created tables:")
        for table in tables:
            print(f"   - {table}")
            
        return True
        
    except Exception as e:
        print(f" Failed to create tables: {e}")
        return False

if __name__ == "__main__":
    success = setup_database()
    
    if success:
        print("\n Database setup complete!")
        print("Next: Run 'python test_groq.py' to test Groq API")
    else:
        sys.exit(1)