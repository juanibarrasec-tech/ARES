import whois
from core.logger import info

def whois_lookup(domain):
    info("WHOIS lookup")
    try:
        w = whois.whois(domain)
        info(f"Registrar: {w.registrar}")
    except:
        info("WHOIS failed")
