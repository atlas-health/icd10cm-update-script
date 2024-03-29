import csv
import gzip
import json
import os

from convert_json import convert_json

# EXISTING FILES PATHS
atlas_codes_gz = './files/icd10.json.gz'
new_codes_json = './files/new_codes.json'


# GENERATED FILES PATHS
icd10_new_json = './files/icd10_new.json'
icd10_new_gz = './files/icd10_new.json.gz'



here = os.path.dirname(os.path.abspath(__file__))
with gzip.open(os.path.join(here, atlas_codes_gz)) as fh:
    codes = json.load(fh)


new_codes_json = os.path.join(here, new_codes_json)
atlas_codes = codes.copy()


def compare_and_fill():
    with open(new_codes_json) as json_new_codes:
        new_codes = json.load(json_new_codes)
        # compare new_codes with atlas_codes
        for code, values in new_codes.items():
            # different description then update
            description = values[1]
            if code in atlas_codes.keys():
                if description != atlas_codes[code][1]:
                    atlas_codes[code] = [True, description]
                else:
                    # do nothing
                    pass
            else:
                # add new code
                atlas_codes[code] = [True, description]
    with open(icd10_new_json, "w") as fh:
        json.dump(atlas_codes, fh)


def count_keys(filename: str):
    counter = 0
    with gzip.open(os.path.join(here, filename)) as fh:
        codes = json.load(fh)

    for key in codes.keys():
        counter += 1
    return counter


def zip_file():
    with open(icd10_new_json, "rb") as f_in:
        with gzip.open(icd10_new_gz, "wb") as f_out:
            f_out.writelines(f_in)


def main():
    print("Counting keys in old file...")
    print(f"{count_keys(atlas_codes_gz)} keys in old file")
    print("Converting txt to json...")
    convert_json()
    print("Comparing and filling... This may take a while.")
    compare_and_fill()
    print("Zipping file...")
    zip_file()
    print("Counting keys in new file...")
    print(f"{count_keys(icd10_new_gz)} keys in new file")


main()
