import json
import os

DATA_FILE = "data/sections.json"


def save_sections(sections: list[str]) -> None:
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=2)


def load_sections() -> list[str]:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
