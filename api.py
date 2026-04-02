from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scanner.nettacker_runner import run_scan
from parser.nettacker_parser import parse_results

app = FastAPI()


# 🔥 CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (for demo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 🔹 Home Route
@app.get("/")
def home():
    return {
        "message": "Attack Surface Management API is running"
    }


# 🔹 AI Summary Function (Demo Level)
def generate_ai_summary(results):

    if not results:
        return "AI Analysis: No vulnerabilities found. Target appears secure."

    count = len(results)

    if count <= 2:
        return f"AI Analysis: {count} minor issues detected. Low risk."
    elif count <= 5:
        return f"AI Analysis: {count} vulnerabilities found. Moderate risk."
    else:
        return f"AI Analysis: {count} vulnerabilities detected. High risk. Immediate action recommended."


# 🔹 Scan Endpoint
@app.get("/scan")
def scan(target: str):

    print(f"[API] Scan request received for: {target}")

    try:
        # Step 1: Run scan
        file_path = run_scan(target)

        # Step 2: Parse results
        results = parse_results(file_path)

        # Step 3: AI Summary
        summary = generate_ai_summary(results)

        return {
            "target": target,
            "total_issues": len(results),
            "results": results,
            "ai_summary": summary
        }

    except Exception as e:
        return {
            "error": str(e)
        }
