import os, json, datetime

class ReportAgent:
    def __init__(self, out="reports"):
        self.out = out
        os.makedirs(self.out, exist_ok=True)

    def generate(self, target, findings):
        ts = datetime.datetime.utcnow().isoformat()
        rep = {
            "target": target,
            "generated_at": ts,
            "total_findings": len(findings),
            "findings": findings
        }
        with open(f"{self.out}/report_{target}.json", "w") as f:
            json.dump(rep, f, indent=2)

        with open(f"{self.out}/report_{target}.md", "w") as f:
            f.write(f"# ARES Report — {target}\n\nGenerated: {ts}\n\n")
            for i, fd in enumerate(findings, 1):
                f.write(f"## Finding {i}\n")
                for k, v in fd.items():
                    f.write(f"- **{k}**: {v}\n")
                f.write("\n")
