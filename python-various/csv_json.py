import csv
import json
from pathlib import Path
from time import gmtime, strftime

csv_file_path = Path.cwd() / "tech-crunch.csv"
json_file_path = Path.cwd() / "tech-crunch.json"


def csv_json(csv_file: Path, json_file: Path):
    json_array = []

    with open(csv_file, encoding="utf-8") as csv_f:
        csv_reader = csv.DictReader(csv_f)
        for row in csv_reader:
            json_array.append(row)

    with open(json_file, "w", encoding="utf-8") as json_f:
        json_str = json.dumps(json_array)
        json_f.write(json_str)


if __name__ == "__main__":
    csv_json(csv_file_path, json_file_path)

print("CSV converted to JSON")
print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))


# Without pathlib
# csv_file_path = "tech-crunch.csv"
# json_file_path = "tech-crunch.json"
