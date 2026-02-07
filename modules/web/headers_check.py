import requests
from core.logger import info, warn, good

SEC_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security"
]

def check_headers(domain):
    url = f"https://{domain}"
    info("Checking security headers")
    try:
        r = requests.get(url, timeout=10)
        headers = r.headers
        for h in SEC_HEADERS:
            if h in headers:
                good(f"{h} present")
            else:
                warn(f"{h} missing")
    except:
        warn("Connection failed")
