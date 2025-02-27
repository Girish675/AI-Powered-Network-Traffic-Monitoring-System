from app.database import get_db

# Test database connection
try:
    db = get_db()
    print("Database connection successful!")
except Exception as e:
    print(f"Error connecting to database: {e}")
finally:
    db.close()
