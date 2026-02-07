import requests
from core.logger import info

def find_subdomains(domain):
    info("Passive subdomain scan (crt.sh)")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        subs = set()
        for entry in data:
            subs.add(entry['name_value'])
        return list(subs)
    except:
        return []
