from datetime import datetime
def log(level, msg):
    print(f"[{datetime.utcnow().isoformat()}] [{level}] {msg}")
