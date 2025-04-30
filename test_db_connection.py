import os
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Helldivers_2_Database.settings')
django.setup()

# Import Django models and database connection
from django.db import connections
from django.db.utils import OperationalError

def test_database_connection():
    print("Testing database connection...")
    
    try:
        # Get the default database connection
        connection = connections['default']
        
        # Attempt to connect to the database
        connection.ensure_connection()
        
        # If we get here, the connection was successful
        print("✅ Database connection successful!")
        
        # Get some database information
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()[0]
            print(f"Database version: {db_version}")
            
            cursor.execute("SELECT current_database();")
            db_name = cursor.fetchone()[0]
            print(f"Database name: {db_name}")
            
            cursor.execute("SELECT current_user;")
            db_user = cursor.fetchone()[0]
            print(f"Connected as user: {db_user}")
            
    except OperationalError as e:
        print(f"❌ Failed to connect to the database: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    test_database_connection()