import re

def rule_based_substitution(text):
    substitution_rules = {
        'gender': ['male', 'female', 'transgender', 'non-binary', 'gender-fluid'],
        'age': ['young', 'middle-aged', 'old', 'elderly', 'teen'],
        'nationality': ['Caucasian', 'American', 'Indian', 'Nigerian', 'African American', 'Asian', 'Hispanic', 'African-American', 'Middle Eastern', 'Hindu', 'European', 'English', 'Japanese', 'Italian', 'South American', 'European', 'Caribbean', 'Canadian', 'Australian', 'Latino'],
        'education level': ['high school', 'bachelor', 'master', 'PhD', 'self-taught'],
        'marital status': ['single', 'married', 'divorced', 'widowed'],
        'personality type': ['introvert', 'extrovert', 'ambivert'],
        'religion': ['Hindu', 'Muslim', 'Christian', 'Christianity', 'Buddhist', 'Jewish', 'Catholic', 'Atheist'],
        'orientation': ['heterosexual', 'homosexual', 'bisexual', 'asexual', 'transgender', 'LGBTQ', 'gay'],
        'disability': ['physically-disabled', 'mentally disabled', 'mental health conditions', 'cognitive impairments', 'visually impaired', 'deaf', 'wheelchair-using', 'autistic', 'hearing-impaired', 'reservist'],
        'pregnant': ['pregnant'],
        'socioeconomic status': ['low-income', 'middle-class', 'high-income'],
        'political affiliation': ['democrat', 'republican', 'liberal', 'conservative', 'socialist', 'libertarian'],
        'immigration status': ['immigrant', 'refugee', 'green card holder', 'undocumented', 'temporary visa holder'],
        'genetic information': ['genetic predisposition'],
        'military or veteran status': ['veteran', 'active duty military', 'civilian'],
        'national origin': ['rural', 'urban'],
        'lifestyle': ['conservative', 'liberal', 'independent'],
        'occupation': ['an engineer', 'a doctor', 'a teacher', 'a software developer', 'a lawyer', 'a nurse', 'an artist', 'a police officer', 'an entrepreneur'],
        'language': ['English', 'Spanish', 'French', 'Chinese', 'Arabic'],
        'political_view': ['conservative', 'liberal', 'socialist', 'libertarian'],
        'family_status': ['parent', 'child-free', 'single parent', 'caregiver'],
        'diet': ['vegetarian', 'vegan', 'omnivore', 'pescatarian', 'paleo'],
        'housing_status': ['homeowner', 'renter', 'homeless', 'living with family']
    }

    for category, substitutes in substitution_rules.items():
        # Join phrases with spaces and escape special characters
        phrases = [re.escape(' '.join(phrase.split())) for phrase in substitutes]
        pattern = r'\b(?:' + '|'.join(phrases) + r')\b'
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            substitute = next((s for s in substitutes if s.lower() != match.group().lower()), None)
            if substitute:
                text = re.sub(match.group(), substitute, text, flags=re.IGNORECASE)
                break  # Exit loop once a substitution is made

    return text

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            cleaned_text = rule_based_substitution(line)
            outfile.write(cleaned_text)

# Replace file paths with the actual file names or paths
input_file = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/one/output_file.txt'
output_file = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/one/fp_testcase_substitution_one.txt'

process_file(input_file, output_file)

