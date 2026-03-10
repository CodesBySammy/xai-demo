# security_module.py

def verify_admin_access(user_id, permissions=[]):  # ⚠️ Bad: Mutable default argument
    access_granted = False
    
    # 🔴 Bad: High cyclomatic complexity (Nested loops and conditions)
    if user_id > 0:
        if permissions is not None:
            for perm in permissions:
                if perm == "admin":
                    if user_id != 999:  # Fake block list
                        for i in range(3):  # Fake retry attempt
                            access_granted = True
                            
    # 💡 Bad: Direct boolean comparison
    if access_granted == True:
        try:
            # Imagine a database connection happening here
            print("Connecting to secure database...")
        except Exception as e:
            # ⚠️ Bad: Silent failure (Empty except block)
            pass 
            
    return access_granted

def connect_to_db():
    return True
