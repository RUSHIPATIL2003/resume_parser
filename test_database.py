import psycopg2
import time
import sys
from config import settings

def test_database_connection():
    """Test if we can connect to PostgreSQL database"""
    print(" Testing Database Connection...")
    print("=" * 50)
    
    max_retries = 5
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}/{max_retries}...")
            
            # Try to connect to PostgreSQL
            conn = psycopg2.connect(settings.DATABASE_URL)
            cursor = conn.cursor()
            
            # Test 1: Check PostgreSQL version
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print(f" PostgreSQL Version: {version[0].split(',')[0]}")
            
            # Test 2: Check if our database exists
            cursor.execute("SELECT datname FROM pg_database WHERE datname = 'resume_parser';")
            db_exists = cursor.fetchone()
            
            if db_exists:
                print(" Database 'resume_parser' exists!")
            else:
                print(" Database 'resume_parser' not found")
                return False
            
            # Test 3: Check if we can access the database
            cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public'
                    LIMIT 1
                );
            """)
            can_access = cursor.fetchone()[0]
            if can_access:
                print(" Can access database tables")
            else:
                print("  No tables found yet (this is normal before setup)")
            
            # Test 4: List all tables (if any exist)
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)
            tables = cursor.fetchall()
            if tables:
                print(" Existing tables:")
                for table in tables:
                    print(f"   - {table[0]}")
            else:
                print(" No tables yet (run setup_database.py to create them)")
            
            cursor.close()
            conn.close()
            
            print("\n Database connection test PASSED!")
            return True
            
        except psycopg2.OperationalError as e:
            if attempt < max_retries - 1:
                print(f"  Connection failed, retrying in 3 seconds...")
                time.sleep(3)
            else:
                print(f" Database connection failed after {max_retries} attempts")
                print(f"Error: {e}")
                print("\n Troubleshooting:")
                print("1. Run: docker compose ps (check if PostgreSQL is running)")
                print("2. Run: docker compose logs postgres (check for errors)")
                print("3. Verify .env file has correct DATABASE_URL")
                print("4. Check if password in .env matches docker-compose.yml")
                return False
        except Exception as e:
            print(f" Unexpected error: {e}")
            return False
    
    return False

if __name__ == "__main__":
    success = test_database_connection()
    
    if success:
        print("\n" + "=" * 50)
        print(" DATABASE IS READY!")
        print("Next: Run 'python setup_database.py' to create tables")
        print("=" * 50)
    else:
        sys.exit(1)