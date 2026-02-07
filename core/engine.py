from core.logger import info, good, warn
from modules.recon.subdomains import find_subdomains
from modules.recon.whois_lookup import whois_lookup
from modules.web.headers_check import check_headers

class AresEngine:
    def __init__(self, target):
        self.target = target

    def run(self, mode):
        info(f"Target: {self.target}")
        info(f"Mode: {mode}")

        if mode == "recon":
            self.recon()
        elif mode == "web":
            self.web()
        else:
            warn("Unknown mode")

    def recon(self):
        info("Running Recon...")
        subs = find_subdomains(self.target)
        whois_lookup(self.target)
        good(f"Subdomains found: {len(subs)}")

    def web(self):
        info("Running Web Checks...")
        check_headers(self.target)
