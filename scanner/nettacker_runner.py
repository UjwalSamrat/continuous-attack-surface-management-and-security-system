import subprocess
import datetime
import os

def run_scan(target):
    print("DEBUG: run_scan called")   # confirm execution

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{target}_{timestamp}.json"

    command = [
        "docker", "run", "--rm",
        "-v", f"{os.getcwd()}:/app",
        "nettacker-local",
        "-i", target,
        "-m", "port_scan",
        "-o", f"/app/{output_file}"
    ]

    print(f"[+] Running scan for {target}")

    subprocess.run(command)

    return output_file
