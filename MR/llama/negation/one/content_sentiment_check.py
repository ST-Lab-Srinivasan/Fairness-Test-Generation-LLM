from textblob import TextBlob
import os

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def get_sentiment_label(polarity):
    if polarity > 0:
        return "Positive"
    else:
        return "Negative"

def read_text(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    folder1 = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/negation/one/output_negation_one/output_3000/'  # Replace with the actual folder path
    folder2 = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/negation/one/output_ST/output_3000/' # Replace with the actual folder path

    files1 = sorted(os.listdir(folder1))
    files2 = sorted(os.listdir(folder2))

    for file in files1:
        if file in files2:
            file1_path = os.path.join(folder1, file)
            file2_path = os.path.join(folder2, file)

            text1 = read_text(file1_path)
            text2 = read_text(file2_path)

            sentiment1 = analyze_sentiment(text1)
            sentiment2 = analyze_sentiment(text2)

            sentiment_label1 = get_sentiment_label(sentiment1)
            sentiment_label2 = get_sentiment_label(sentiment2)

            print(f"File: {file}")
            print(f"Sentiment of File 1: {sentiment_label1}")
            print(f"Sentiment of File 2: {sentiment_label2}\n")
        else:
            print(f"File: {file} does not have a corresponding file in folder 2.\n")

if __name__ == "__main__":
    main()
