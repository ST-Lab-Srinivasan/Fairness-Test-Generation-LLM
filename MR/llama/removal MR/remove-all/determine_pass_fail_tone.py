import re
import os

# Define the path to the directory containing the text file
directory_path = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/removal MR/remove-all/'  # Replace this with the actual path
file_name = 'result_tone_check.txt'
file_path = os.path.join(directory_path, file_name)

# Reading the file content
try:
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Split the content into sections based on the file names
    sections = re.split(r'(File:\s+response_\d+\.txt)', file_content)
    results = {}

    # Iterate through the sections and process tones
    for i in range(1, len(sections), 2):
        file_header = sections[i].strip()
        section = sections[i + 1].strip()

        # Extract tones using regex
        tones = re.findall(r'Tone of File \d+: (\w+ Tone)', section)
        if len(tones) == 2:
            file_name = re.search(r'response_\d+\.txt', file_header).group()
            results[file_name] = "pass" if tones[0] == tones[1] else "fail"
        else:
            results[file_header] = "invalid data"

    # Print the results
    for file, result in results.items():
        print(f"{file}: {result}")

except FileNotFoundError:
    print(f"The file {file_name} was not found in the directory {directory_path}. Please check the path and try again.")

