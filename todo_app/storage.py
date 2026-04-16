import json
import os

FILENAME = "tasks.json"

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent = 4)
    print("💾 Tasks saved!")    

def load_tasks():
    if not os.path.exists(FILENAME):
        return []    #First time running, no file yet

    with open(FILENAME, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Save file is corrupted. Starting fresh.")
            return []        