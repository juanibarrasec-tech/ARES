import requests
from core.config import USER_AGENT, TIMEOUT

def fetch(url):
    try:
        r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT)
        return r.text, r.headers
    except:
        return None, None
