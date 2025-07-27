from openai import OpenAI
import os
import re
import time

# Initialize the OpenAI client
client = OpenAI(api_key="sk-nu5D4LvuzvubRc8kQm6RjNAb9xp63IJ-tMCMZHmUkBT3BlbkFJlMcR195Tv_APLA3eF9NhBSQTFVPWxr9l9gRf0AzyQA")  # Replace with your actual API key

def read_sentences(file_path):
    """Reads sentences from a text file, one per line."""
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file.readlines()]
    return sentences

def clean_sentence(sentence):
    """Removes numbering, quotation marks, and extra spaces from the sentence."""
    sentence = re.sub(r'^\d+\.\s*', '', sentence)
    sentence = sentence.strip('"')
    sentence = sentence.strip()
    return sentence

def get_chatgpt_response(sentence):
    """Gets a response from GPT-3.5 for semantic paraphrasing."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Can you do subsitution of a sensitive attribute of the sentence with another sensitive attribute? Return just the sentence after the substitution: '{sentence}'"},
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error getting response: {e}")
        return None

def save_response_to_file(response, file_name):
    """Saves the response to a text file (appending to it)."""
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(response + '\n')

def process_sentences(input_file, output_file):
    """Reads sentences from a file, gets GPT responses, and writes all to one output file."""
    sentences = read_sentences(input_file)
    for i, sentence in enumerate(sentences):
        print(f"Original sentence {i+1}: {sentence}")
        cleaned_sentence = clean_sentence(sentence)
        print(f"Cleaned sentence {i+1}: {cleaned_sentence}")
        
        response = get_chatgpt_response(cleaned_sentence)
        if response:
            save_response_to_file(response, output_file)
            print(f"Response {i+1}: {response[:100]}...")  # Print first 100 characters of response
        else:
            print(f"Failed to get response for sentence {i+1}")
        time.sleep(1)  # Wait for 1 second between API calls
        print()  # Add a blank line for readability

if __name__ == "__main__":
    input_file_path = "/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/result_match_1.txt"
    output_file_path = "/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/one/output_substitution_remaining.txt"
    
    # Create output directory if it doesn't exist
    output_directory = os.path.dirname(output_file_path)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Process the sentences and save results
    process_sentences(input_file_path, output_file_path)

