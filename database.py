# database.py
import sqlite3
import logging

def get_insecure_connection():
    """Returns a database connection. Contains a silent failure bug."""
    try:
        conn = sqlite3.connect("enterprise_fleet.db")
        return conn
    except Exception:
        pass # 🐛 AST Engine will catch this silent failure
