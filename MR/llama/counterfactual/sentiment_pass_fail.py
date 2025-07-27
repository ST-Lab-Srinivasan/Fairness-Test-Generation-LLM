import re

def compare_sentiments(content):
    # Extract file name and sentiments
    match = re.search(r'File: (.+)\nSentiment of File 1: (\w+)\nSentiment of File 2: (\w+)', content)
    if not match:
        return "Error: Could not parse file content"
    
    filename, sentiment1, sentiment2 = match.groups()
    
    if sentiment1 == sentiment2 == 'Positive':
        return f"{filename}: PASS"
    else:
        return f"{filename}: FAIL (File 1: {sentiment1}, File 2: {sentiment2})"

# Read and process the text file
with open('/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/counterfactual/result_Sentiment_gpt_check.txt', 'r') as file:
    content = file.read()

# Split content into sections for each file
file_sections = content.split('File: ')[1:]  # Skip the first empty split

for section in file_sections:
    result = compare_sentiments('File: ' + section.strip())
    print(result)
