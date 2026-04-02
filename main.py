from scanner.nettacker_runner import run_scan
from scanner.target_loader import load_targets
from parser.nettacker_parser import parse_results

def main():

    print("🚀 Program started...")   # DEBUG LINE

    targets = load_targets()

    if not targets:
        print("No targets found!")
        return

    for target in targets:

        print(f"\n[+] Scanning: {target}")

        file = run_scan(target)
        results = parse_results(file)

        print("\nParsed Results:\n")

        for r in results:
            print(r)

if __name__ == "__main__":
    main()
