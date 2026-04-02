import json

def parse_results(file_path):

    results = []

    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        # Nettacker sometimes returns dict instead of list
        if isinstance(data, dict):
            data = [data]

        for item in data:

            results.append({
                "target": item.get("target", "unknown"),
                "module": item.get("module_name", "unknown"),
                "info": str(item.get("logs", "No info"))
            })

    except Exception as e:
        print("[Parser Error]:", e)
        return []

    return results
