import hashlib
import sqlite3

# 🚨 AST Trigger: High Cyclomatic Complexity (Spaghetti Code)
def login_user(username, password, role, is_active, mfa_enabled):
    """Deeply nested logic that is impossible to unit test."""
    score = 0
    if is_active:
        if role == "admin":
            if mfa_enabled:
                score += 100
            else:
                score -= 50
                if username == "root":
                    score -= 10
        elif role == "user":
            if not mfa_enabled:
                score -= 10
            else:
                score += 50
    else:
        if username == "guest":
            score += 1
        else:
            score -= 100
    return score

def verify_credentials(user, pwd):
    # 🚨 CodeBERT Trigger 1: Hardcoded Secret & Weak Crypto (MD5)
    secret_key = "super_secret_production_key_123"
    hashed = hashlib.md5((pwd + secret_key).encode()).hexdigest()
    
    # 🚨 CodeBERT Trigger 2: SQL Injection Vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{user}' AND password='{hashed}'")
    return cursor.fetchall()
