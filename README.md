# ARES — Legal Bug Bounty Framework

ARES is a lightweight, modular and legal-first Bug Bounty automation framework designed for reconnaissance, surface mapping and safe passive analysis.

## Philosophy

ARES does NOT exploit, attack or damage targets. It automates safe and legal Bug Bounty workflow:

Recon → Surface Mapping → Passive Checks → Evidence → Report

## Legal Notice

Use ONLY on:
- Authorized Bug Bounty programs
- Your own labs
- Targets with written permission

You are responsible for how you use ARES.

## Installation (Termux / Linux)

```bash
pkg update && pkg upgrade -y
pkg install python git -y

git clone https://github.com/juanibarrasec-tech/ARES.git
cd ARES

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Usage

```bash
python cli/ares.py -t example.com -m recon
```

### Modes:
- **recon** → subdomains, whois, tech fingerprint
- **web** → headers + basic security checks
- **osint** → public exposure

## Roadmap
- Subdomain takeover detector
- JS secrets finder
- API mapper
- Auto CVSS scoring
- HTML/PDF report generator

---
ARES — Built for real hunters
