import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_json(filename):
    path = DATA_DIR / filename
    with path.open(encoding="utf-8") as f:
        return json.load(f)

def load_players():
    return load_json("players.json")

def load_weapons():
    return load_json("weapons.json")

def load_armors():
    return load_json("armors.json")

def load_enemies():
    return load_json("enemies.json")

def load_rooms():
    return load_json("rooms.json")

def load_difficulties():
    return load_json("difficulty.json")
