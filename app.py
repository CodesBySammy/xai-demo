def process_user_data(data=[]):  # Bad: Mutable default argument
    if data == True:             # Bad: Direct boolean comparison
        try:
            for i in range(100):
                for j in range(100):
                    if i == j:
                        print(i * j) # Highly complex nested logic
        except Exception as e:
            pass                     # Bad: Silent failure
