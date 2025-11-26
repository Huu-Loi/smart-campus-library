import json
import os

DATA_FILE = "library_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"books": [], "members": [], "loans": []}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"books": [], "members": [], "loans": []}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
