"""Script para convertir un archivo CSV a JSON"""

import csv
import json


def convert_csv_2_json(input_file):
    """Converts a CSV file to a JSON file"""

    output_file = input_file.replace(".csv", ".json")
    data = []

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # ui.notify("The file was transformed successfully!")


convert_csv_2_json("files/drivers.csv")

