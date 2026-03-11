import sqlite3
import hashlib
import requests

# 🚨 Trigger 1: AST State Bug (Mutable Default Argument)
def process_scooter_telemetry(battery_level, active_errors=[]):
    """Processes incoming data from the electric vehicle fleet."""
    if battery_level < 20:
        active_errors.append("LOW_BATTERY")
    return active_errors

# 🚨 Trigger 2: CodeBERT Semantic Vulnerabilities
def authenticate_rider(username, password):
    """Authenticates a user for the mobile app."""
    # CodeBERT will flag this hardcoded secret and insecure MD5 hashing
    api_secret = "super_secret_admin_key_12345" 
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    # CodeBERT will absolutely flag this SQL Injection risk
    db = sqlite3.connect("fleet_data.db")
    cursor = db.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{hashed_password}'"
    
    # 🚨 Trigger 3: AST Reliability Bug (Silent Failure)
    try:
        cursor.execute(query)
        return cursor.fetchone()
    except Exception:
        pass  # 🐛 SILENT FAILURE: The database crashes, but hides the error from logs

# 🚨 Trigger 4: AST High Cyclomatic Complexity (Spaghetti Code)
def calculate_optimal_route(traffic_data, weather, destination, time_of_day):
    """Finds the best route. This is too complex and impossible to unit test."""
    route_score = 0
    if traffic_data == "high":
        if weather == "rain":
            if time_of_day == "rush_hour":
                for road in ["main_st", "highway_1", "back_alley"]:
                    if road == "highway_1":
                        route_score -= 10
                    elif road == "back_alley":
                        route_score += 5
            elif time_of_day == "evening":
                if destination == "downtown":
                    route_score -= 5
        elif weather == "clear":
            if time_of_day == "morning":
                route_score += 20
    elif traffic_data == "low":
        if weather == "snow":
            for road in ["main_st", "highway_1"]:
                if road == "main_st":
                    route_score -= 2
        else:
            route_score += 50
            if destination == "suburbs":
                route_score += 10
            elif destination == "airport":
                route_score += 15
                
    return route_score 
    
