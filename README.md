# Update ICD10-CM codes

### 1. Download the latest ICD10-CM codes from the CMS website
> Website: https://www.cms.gov/medicare/icd-10/2023-icd-10-cm

> You will probably need to download all the options in order to get the one you need.

### 2. Search for the file
> The file name will looks like this: `icd10cm_codes_2024.txt`

### 3. Copy the file to the source folder of this project

### 4. Copy the icd10.json.gz in the icd-cm repository to the source folder of this project

### 5. Run the script

```bash
python3 update_icd10cm.py
```

### Step 6. Copy the icd10_new.json.gz to the icd-cm repository rename it to icd10.json.gz and replace the old one