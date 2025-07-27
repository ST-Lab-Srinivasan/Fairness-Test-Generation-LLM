import os
import shutil
import re

# Define source and destination folders
source_folder = "/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/all/output_fp_substitution_all/output_fp"
destination_folder = "/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/all/output_fp_substitution_all/output_fp_1"

# Ensure destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Helper function to extract numeric value from file name
def extract_numeric(name):
    match = re.search(r'\d+', name)
    return int(match.group()) if match else float('inf')

# Get a sorted list of files in the source folder
files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
files.sort(key=extract_numeric)  # Sort by numeric order (e.g., response_1.txt, response_2.txt)

# Track the total files copied
files_copied = 0
limit = 14474  # Limit for the number of files to copy

# Copy files to the destination folder
for file_name in files:
    if files_copied >= limit:
        break

    source_file_path = os.path.join(source_folder, file_name)
    destination_file_path = os.path.join(destination_folder, file_name)
    
    shutil.copy(source_file_path, destination_file_path)
    files_copied += 1

print(f"Copied {files_copied} files from '{source_folder}' to '{destination_folder}'.")

