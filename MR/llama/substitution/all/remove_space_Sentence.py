import re

def format_sentences_to_new_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()

        # Split text into sentences using regex
        sentences = re.split(r'(?<=[.?!])\s+', text.strip())

        # Write each sentence on a new line in the output file
        with open(output_file, 'w') as file:
            file.write('\n'.join(sentences))

        print(f"File processed successfully. Sentences saved in '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_file = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/all/matching_statement.txt'  # Replace with the path to your input file
output_file = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/all/output_sentence_match.txt'  # Replace with the desired output file name
format_sentences_to_new_lines(input_file, output_file)

