import json

# 🚨 AST Trigger: Mutable Default Argument (The AI will generate an Auto-Fix for this!)
def process_sensor_data(sensor_id, readings=[]):
    """This will cause memory leaks between function calls."""
    readings.append(sensor_id)
    return readings

def parse_telemetry(raw_payload):
    # 🚨 AST Trigger: Silent Failure
    try:
        data = json.loads(raw_payload)
        return data
    except Exception:
        pass 
        # The AI will catch this bare except blocking the logs
