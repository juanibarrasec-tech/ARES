def run(engine):
    # Solo sugerencias pasivas (no scraping agresivo)
    engine.add_finding({"type": "osint", "detail": f"Use dorks: site:{engine.target} ext:env OR ext:log"})
