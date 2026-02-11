from utils.safe_request import get

def run(engine):
    r = get(f"http://{engine.target}")
    if not r: return
    engine.add_finding({"type": "headers", "server": r.headers.get("Server")})
