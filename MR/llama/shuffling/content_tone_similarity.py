from textblob import TextBlob
import os

def analyze_tone(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return 'Positive Tone'
    elif polarity < -0.1:
        return 'Negative Tone'
    else:
        return 'Neutral Tone'

def read_text(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    folder1 = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/shuffling/ST_output_3000/'  # Replace with the actual folder path
    folder2 = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/shuffling/shuffling_llama_proposed/output_shuffling/' # Replace with the actual folder path

    files1 = sorted(os.listdir(folder1))[:3228]  # Limit to the first 14,474 files
    files2 = sorted(os.listdir(folder2))

    for file in files1:
        if file in files2:
            file1_path = os.path.join(folder1, file)
            file2_path = os.path.join(folder2, file)

            text1 = read_text(file1_path)
            text2 = read_text(file2_path)

            tone1 = analyze_tone(text1)
            tone2 = analyze_tone(text2)

            print(f"File: {file}")
            print(f"Tone of File 1: {tone1}")
            print(f"Tone of File 2: {tone2}\n")
        else:
            print(f"File: {file} does not have a corresponding file in folder 2.\n")

if __name__ == "__main__":
    main()

