from transformers import pipeline
import os

# Load pre-trained BERT model for sentiment analysis
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment_with_bert(text):
    # Perform sentiment analysis using BERT
    sentiment = sentiment_analyzer(text[:512])  # Limit input to 512 tokens (BERT's max input length)
    label = sentiment[0]['label']
    score = sentiment[0]['score']
    return label, score

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def main():
    folder1 = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/all/output_substitution_all/output_1/'  # Replace with the actual folder path
    folder2 = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/negation/all/output_ST/output_3000/'  # Replace with the actual folder path

    files1 = sorted(os.listdir(folder1))
    files2 = sorted(os.listdir(folder2))

    for file in files1:
        if file in files2:
            file1_path = os.path.join(folder1, file)
            file2_path = os.path.join(folder2, file)

            text1 = read_text(file1_path)
            text2 = read_text(file2_path)

            sentiment1, score1 = analyze_sentiment_with_bert(text1)
            sentiment2, score2 = analyze_sentiment_with_bert(text2)

            print(f"File: {file}")
            print(f"Sentiment of File 1: {sentiment1} (Confidence: {score1:.4f})")
            print(f"Sentiment of File 2: {sentiment2} (Confidence: {score2:.4f})\n")
        else:
            print(f"File: {file} does not have a corresponding file in folder 2.\n")

if __name__ == "__main__":
    main()

