from transformers import pipeline
import os

# Load pre-trained BERT model fine-tuned for tone analysis (emotion detection)
tone_analyzer = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def analyze_tone_with_bert(text):
    # Perform tone analysis using the tone/emotion model
    tone = tone_analyzer(text, truncation=True, max_length=512)  # Automatically handles long inputs

    label = tone[0]['label']
    score = tone[0]['score']
    return label, score

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def main():

    folder1 = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/counterfactual/output_counterfactual_ft/'  # Replace with the actual folder path
    #folder1 = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/counterfactual/output_fp_rerun_counterfactual_1/'  # Replace with the actual folder path

    folder2 = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/counterfactual/output_counterfactual_st/' # Replace with the actual folder path

    files1 = sorted(os.listdir(folder1))
    files2 = sorted(os.listdir(folder2))

    for file in files1:
        if file in files2:
            file1_path = os.path.join(folder1, file)
            file2_path = os.path.join(folder2, file)

            text1 = read_text(file1_path)
            text2 = read_text(file2_path)

            tone1, score1 = analyze_tone_with_bert(text1)
            tone2, score2 = analyze_tone_with_bert(text2)

            print(f"File: {file}")
            print(f"Tone of File 1: {tone1}")
            print(f"Tone of File 2: {tone2}\n")
        else:
            print(f"File: {file} does not have a corresponding file in folder 2.\n")

if __name__ == "__main__":
    main()

