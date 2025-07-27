import re
import random

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

    # Create a pattern for all sensitive attributes
    all_phrases = []
    for substitutes in substitution_rules.values():
        all_phrases.extend([re.escape(' '.join(phrase.split())) for phrase in substitutes])
    pattern = r'\b(?:' + '|'.join(all_phrases) + r')\b'
    
    # Find all matches
    matches = list(re.finditer(pattern, text, flags=re.IGNORECASE))
    
    # Substitute all matches, starting from the end to preserve indices
    for match in reversed(matches):
        matched_text = match.group()
        for category, substitutes in substitution_rules.items():
            if any(sub.lower() == matched_text.lower() for sub in substitutes):
                # Choose a random substitute from the same category
                substitute = random.choice([s for s in substitutes if s.lower() != matched_text.lower()])
                text = text[:match.start()] + substitute + text[match.end():]
                break
    
    return text

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            cleaned_text = rule_based_substitution(line)
            outfile.write(cleaned_text)

# Replace file paths with the actual file names or paths
input_file = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/all/output_file.txt'
output_file = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/all/fp_testcase_substitution_all.txt'

process_file(input_file, output_file)
import re
import random

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

    # Create a pattern for all sensitive attributes
    all_phrases = []
    for substitutes in substitution_rules.values():
        all_phrases.extend([re.escape(' '.join(phrase.split())) for phrase in substitutes])
    pattern = r'\b(?:' + '|'.join(all_phrases) + r')\b'
    
    # Find all matches
    matches = list(re.finditer(pattern, text, flags=re.IGNORECASE))
    
    # Substitute all matches, starting from the end to preserve indices
    for match in reversed(matches):
        matched_text = match.group()
        for category, substitutes in substitution_rules.items():
            if any(sub.lower() == matched_text.lower() for sub in substitutes):
                # Choose a random substitute from the same category
                substitute = random.choice([s for s in substitutes if s.lower() != matched_text.lower()])
                text = text[:match.start()] + substitute + text[match.end():]
                break
    
    return text

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            cleaned_text = rule_based_substitution(line)
            outfile.write(cleaned_text)

# Replace file paths with the actual file names or paths
input_file = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/all/output_file.txt'
output_file = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/propsed approach/substitution/all/fp_testcase_substitution_all.txt'

process_file(input_file, output_file)

