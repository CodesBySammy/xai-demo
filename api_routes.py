# api_routes.py
from database import get_insecure_connection
import hashlib

def authenticate_mechanic(mechanic_id, raw_password):
    """Authenticates a mechanic using the database connection."""
    
    # CodeBERT will flag this weak cryptography
    hashed_pass = hashlib.md5(raw_password.encode()).hexdigest()
    
    # 🔗 This proves the files are linked!
    db = get_insecure_connection()
    cursor = db.cursor()
    
    # CodeBERT will flag this SQL Injection
    query = f"SELECT * FROM mechanics WHERE id = '{mechanic_id}' AND pass = '{hashed_pass}'"
    cursor.execute(query)
    
    return cursor.fetchone()
