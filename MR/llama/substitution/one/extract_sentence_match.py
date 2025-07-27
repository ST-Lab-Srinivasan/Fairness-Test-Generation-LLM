import re

# Path to the input file
input_file = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/result_match_1.txt'
output_file = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/output_match.txt'

# Function to clean the lines
def clean_lines(input_path, output_path):
    with open(input_path, 'r') as file:
        lines = file.readlines()

    # Regular expression to match and remove "Line <number> | <number> |"
    cleaned_lines = [re.sub(r"^Line\s+\d+\s+\|\s+\d+\s+\|", "", line).strip() for line in lines]

    # Write the cleaned lines to a new file
    with open(output_path, 'w') as file:
        file.writelines(line + '\n' for line in cleaned_lines)

# Clean the lines in the text file
clean_lines(input_file, output_file)

print(f"Cleaned lines have been written to {output_file}")

