import json

def generate_payload(text=None):
    payload = {
        "id": "5cc704bc-5c1f-4726-be18-2fc6fb55fa81",
        "ts": 1735417556973
    }
    
    if text is not None:
        payload["text"] = text

    return json.dumps(payload)