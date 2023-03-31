import csv

# define the input and output files
input_file = "icd10cm_codes_addenda_2023.txt"
output_file = "new_codes.csv"

headers = ["Action", "Code", "Description"]


def convert_csv():
    # open the input and output files
    with open(input_file, "r") as f_in, open(output_file, "w", newline="") as f_out:
        # create a CSV writer with semicolon delimiter
        writer = csv.writer(f_out, delimiter=";")
        # write the header
        writer.writerow(headers)
        # iterate over each line in the input file
        for line in f_in:
            # remove leading/trailing whitespace and split the line into parts
            parts = line.strip().split()
            # check if the line is valid (must have at least three parts)
            if len(parts) >= 3:
                # extract the action, code, and description
                if parts[0].startswith("Revise"):
                    # change :
                    parts[1] = parts[1].rstrip(":")
                    action = f"{parts[0]} {parts[1]}"
                    code = parts[2]
                    description = " ".join(parts[3:])
                else:
                    action = parts[0].rstrip(":")
                    code = parts[1]
                    description = " ".join(parts[2:])
                # write the data to the CSV file
                writer.writerow([action, code, description])
