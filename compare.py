import csv
import gzip
import json
import os
from typing import Optional

here = os.path.dirname(os.path.abspath(__file__))
with gzip.open(os.path.join(here, "icd10.json.gz")) as fh:
    codes = json.load(fh)


counting = 0
## read icd10cm_codes_2023.csv
icd10cm_codes_2023_csv = os.path.join(here, "icd10cm_codes_2023.csv")
with open(icd10cm_codes_2023_csv) as csv_icd10cm_codes_2023:
    for column in csv.reader(csv_icd10cm_codes_2023, delimiter=";"):
        if column[0] not in codes.keys():
            with open("icd10cm_codes_2023_not_in_icd10.txt", "a") as fh:
                fh.write(column[0] + "\n")
            counting += 1

print(counting)
