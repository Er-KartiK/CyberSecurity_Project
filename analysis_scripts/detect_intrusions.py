import json

with open("zeek_logs/http.log") as f:
    http_event = json.load(f)
    if "malicious" in http_event["host"] or "exe" in http_event["uri"]:
        print(f"Possible malware download from {http_event['host']}{http_event['uri']}")
