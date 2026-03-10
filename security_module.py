def process_data(user_input, cache={}): # State bug
    # Resource leak
    log_file = open("system.log", "w") 
    log_file.write(user_input)
    
    try:
        # Critical security flaw (RCE)
        eval(user_input)
    except Exception:
        # Reliability risk
        pass
        
    return True
