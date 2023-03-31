import csv
import gzip
import json
import os

from convert_csv import convert_csv

here = os.path.dirname(os.path.abspath(__file__))
with gzip.open(os.path.join(here, "icd10.json.gz")) as fh:
    codes = json.load(fh)

new_codes_csv = os.path.join(here, "new_codes.csv")

code_copy = codes.copy()


def compare_and_fill():
    with open(new_codes_csv) as csv_new_codes:
        reader = csv.DictReader(csv_new_codes, delimiter=";")
        for column in reader:
            action = column["Action"]
            code = column["Code"]
            description = column["Description"]
            for key, value in code_copy.items():
                if action == "Delete":
                    # do nothing
                    pass
                elif action == "Add":
                    codes[code] = [True, description]
                elif action == "Revise from":
                    if code == key:
                        codes.pop(key)
                elif action == "Revise to":
                    codes[code] = [True, description]
    with open("icd10_new.json", "w") as fh:
        json.dump(codes, fh)


# count keys in icd10_new.json
def count_keys():
    counter = 0
    with gzip.open(os.path.join(here, "icd10.json.gz")) as fh:
        codes = json.load(fh)

    for key in codes.keys():
        counter += 1
    print(counter)


def zip_file():
    with open("icd10_new.json", "rb") as f_in:
        with gzip.open("icd10_new.json.gz", "wb") as f_out:
            f_out.writelines(f_in)


def main():
    # count_keys()
    print("Converting csv to json")
    convert_csv()
    print("Comparing and filling... This may take a while.")
    compare_and_fill()
    print("Zipping file")
    zip_file()


main()
