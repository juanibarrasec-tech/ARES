import whois
def run(engine):
    try:
        w = whois.whois(engine.target)
        engine.add_finding({"type": "whois", "registrar": str(w.registrar)})
    except:
        pass
