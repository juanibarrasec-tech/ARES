import argparse
from core.engine import AresEngine
from core.pipeline import build_pipeline
from core.logger import log
from utils.validator import valid_domain

def main():
    p = argparse.ArgumentParser()
    p.add_argument("-t", "--target", required=True)
    p.add_argument("--auto", action="store_true")
    args = p.parse_args()

    if not valid_domain(args.target):
        log("ERROR", "Dominio inválido")
        return

    engine = AresEngine()
    engine.set_target(args.target)

    pipeline = build_pipeline(auto=args.auto)
    engine.run(pipeline)

if __name__ == "__main__":
    main()
