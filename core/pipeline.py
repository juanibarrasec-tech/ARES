from modules.recon.subdomains import run as subdomains
from modules.recon.whois import run as whois
from modules.web.headers import run as headers
from modules.osint.dorks_passive import run as dorks
from modules.osint.shodan_lookup import run as shodan
from modules.osint.wayback import run as wayback

def build_pipeline(auto=False):
    base = [subdomains, whois, headers]
    if auto:
        base += [dorks, shodan, wayback]
    return base
