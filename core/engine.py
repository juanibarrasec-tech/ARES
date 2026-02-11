import json, os, time
from core.logger import log
from agents.report_agent import ReportAgent

class AresEngine:
    def __init__(self):
        self.target = None
        self.findings = []
        self.start = time.time()

    def set_target(self, t):
        self.target = t

    def add_finding(self, f):
        self.findings.append(f)

    def save(self):
        os.makedirs("data", exist_ok=True)
        with open("data/results.json", "w") as f:
            json.dump({
                "target": self.target,
                "duration": time.time() - self.start,
                "findings": self.findings
            }, f, indent=2)

    def run(self, pipeline):
        for stage in pipeline:
            try:
                stage(self)
            except Exception as e:
                log("ERROR", str(e))
        self.save()
        ReportAgent().generate(self.target, self.findings)
