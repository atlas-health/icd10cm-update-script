import json

# define the input and output files
input_file = "icd10cm_codes_2024.txt"
output_file = "new_codes.json"
def convert_json():
    # open the input and output files
    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        codes = {}
        for line in f_in:
            # remove leading/trailing whitespace and split the line into parts
            parts = line.strip().split()
            code = parts[0]
            description = " ".join(parts[1:])
            codes[code] = [True, description]
        json.dump(codes, f_out)


convert_json()