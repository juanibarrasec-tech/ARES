from core.engine import AresEngine
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True, help="Authorized target")
    parser.add_argument("-m", "--mode", default="recon", help="recon / web")

    args = parser.parse_args()

    engine = AresEngine(args.target)
    engine.run(args.mode)

if __name__ == "__main__":
    main()
