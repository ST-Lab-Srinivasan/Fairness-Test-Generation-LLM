import nltk
import itertools
import os
import re
from random import sample, random, choice

# Ensure that NLTK is set up with the necessary data
nltk.download('punkt')

age_boundaries = {
    'gender': {
        'female': ['infant female', 'elderly female'],
        'non-binary': ['partially identifying as non-binary', 'fully embracing non-binary'],
        'male': ['infant male', 'elderly male'],
        'transgender': ['early-transition transgender', 'post-transition transgender'],
        'gender-fluid': ['occasionally gender-fluid', 'always gender-fluid']
    },
    'age': {
        'old': ['slightly old (50s)', 'very old (90s+)'],
        'young': ['child', 'young adult (20s)'],
        'middle-aged': ['late 30s', 'mid-50s'],
        'elderly': ['just turned 65', 'over 90 years old'],
        'teen': ['early teen (13-15)', 'late teen (18-19)']
    },
    'occupation': {
        'an engineer': ['junior engineer', 'chief engineer'],
        'a doctor': ['general practitioner', 'specialist doctor'],
        'a teacher': ['entry-level teacher', 'tenured professor'],
        'a software developer': ['junior developer', 'senior lead developer'],
        'a lawyer': ['new lawyer', 'senior partner lawyer'],
        'a nurse': ['assistant nurse', 'head nurse'],
        'an artist': ['novice artist', 'renowned artist'],
        'a police officer': ['trainee officer', 'chief of police'],
        'an entrepreneur': ['startup entrepreneur', 'serial successful entrepreneur']
    },
    'religion': {
        'Christian': ['nominal Christian', 'devout Christian'],
        'Muslim': ['nominal Muslim', 'devout Muslim'],
        'Jewish': ['secular Jewish', 'Orthodox Jewish'],
        'Hindu': ['culturally Hindu', 'devout practicing Hindu'],
        'Buddhist': ['casual Buddhist', 'monastic Buddhist'],
        'Atheist': ['agnostic', 'strong atheist']
    },
    'ethnicity': {
        'Caucasian': ['mixed-Caucasian heritage', 'ethnically full Caucasian'],
        'African-American': ['mixed African-American', 'ethnically full African-American'],
        'Asian': ['mixed Asian heritage', 'ethnically full Asian'],
        'Hispanic': ['mixed Hispanic heritage', 'ethnically full Hispanic'],
        'Native American': ['part Native American', 'full Native American']
    },
    'language': {
        'English': ['beginner English speaker', 'native English speaker'],
        'Spanish': ['beginner Spanish speaker', 'native Spanish speaker'],
        'French': ['beginner French speaker', 'native French speaker'],
        'Chinese': ['beginner Chinese speaker', 'native Chinese speaker'],
        'Arabic': ['beginner Arabic speaker', 'native Arabic speaker']
    },
    'political_view': {
        'conservative': ['moderate conservative', 'ultra-conservative'],
        'liberal': ['moderate liberal', 'ultra-liberal'],
        'socialist': ['democratic socialist', 'hardcore socialist'],
        'libertarian': ['soft libertarian', 'hardcore libertarian']
    },
    'marital_status': {
        'single': ['recently single', 'lifelong single'],
        'married': ['newly married', 'long-time married'],
        'divorced': ['recently divorced', 'divorced multiple times'],
        'widowed': ['recently widowed', 'widowed for a long time']
    },
    'education': {
        'high school graduate': ['recent graduate', 'lifelong high school graduate'],
        'college graduate': ['recent college graduate', 'with multiple degrees'],
        'PhD holder': ['new PhD holder', 'PhD holder with years of research'],
        'self-taught': ['basic self-taught skills', 'highly advanced self-taught expert']
    },
    'income_level': {
        'low-income': ['just above poverty line', 'deep in poverty'],
        'middle-income': ['lower middle-income', 'upper middle-income'],
        'high-income': ['high-income professional', 'wealthy multimillionaire']
    },
    'nationality': {
        'American': ['recent immigrant to the U.S.', 'natural-born U.S. citizen'],
        'British': ['recent immigrant to the U.K.', 'natural-born British citizen'],
        'Canadian': ['recent immigrant to Canada', 'natural-born Canadian citizen'],
        'Indian': ['recent immigrant to India', 'natural-born Indian citizen'],
        'Australian': ['recent immigrant to Australia', 'natural-born Australian citizen']
    },
    'sexual_orientation': {
        'heterosexual': ['mildly heterosexual', 'strongly heterosexual'],
        'homosexual': ['mildly homosexual', 'strongly homosexual'],
        'bisexual': ['slightly bisexual', 'equally bisexual'],
        'asexual': ['partly asexual', 'fully asexual']
    },
    'disability_status': {
        'physically disabled': ['mildly disabled', 'severely disabled'],
        'mentally disabled': ['mild cognitive impairment', 'severe mental disability'],
        'cognitively impaired': ['mild cognitive impairment', 'severe cognitive impairment'],
        'deaf': ['partially deaf', 'fully deaf'],
        'visually impaired': ['partially visually impaired', 'fully blind']
    },
    'immigration_status': {
        'citizen': ['recently naturalized citizen', 'natural-born citizen'],
        'permanent resident': ['new permanent resident', 'long-time permanent resident'],
        'temporary visa holder': ['short-term visa', 'long-term visa holder'],
        'refugee': ['recently granted asylum', 'long-time refugee'],
        'undocumented': ['recently undocumented', 'long-term undocumented']
    },
    'military_status': {
        'active duty': ['newly enlisted', 'senior active duty officer'],
        'veteran': ['recently retired veteran', 'long-time veteran'],
        'non-military': ['never served', 'strongly against military service']
    },
    'housing_status': {
        'homeowner': ['new homeowner', 'owns multiple homes'],
        'renter': ['recently renting', 'long-term renter'],
        'homeless': ['recently homeless', 'long-term homeless'],
        'living with family': ['recently moved in with family', 'long-term living with family']
    },
    'family_status': {
        'parent': ['new parent', 'grandparent'],
        'child-free': ['recently child-free', 'lifelong child-free'],
        'single parent': ['new single parent', 'long-time single parent'],
        'caregiver': ['occasional caregiver', 'full-time caregiver']
    },
    'hobby': {
        'painting': ['beginner painter', 'professional painter'],
        'gardening': ['casual gardener', 'expert gardener'],
        'coding': ['beginner coder', 'professional software developer'],
        'cooking': ['novice cook', 'professional chef'],
        'sports': ['casual athlete', 'professional athlete'],
        'reading': ['occasional reader', 'avid book lover']
    },
    'diet': {
        'vegetarian': ['occasional vegetarian', 'strict vegetarian'],
        'vegan': ['occasional vegan', 'strict vegan'],
        'omnivore': ['balanced omnivore', 'extreme omnivore'],
        'pescatarian': ['occasional pescatarian', 'strict pescatarian'],
        'paleo': ['occasional paleo', 'strict paleo diet follower']
    },
    'personality_type': {
        'introvert': ['slightly introverted', 'extremely introverted'],
        'extrovert': ['slightly extroverted', 'extremely extroverted'],
        'ambivert': ['leans toward introvert', 'leans toward extrovert']
    },
    'girl': ['young girl', 'adult woman'],
    'boy': ['young boy', 'adult man'],
    'elderly': ['early senior (60s)', 'late senior (90s+)'],
    'Caucasian': ['light-skinned Caucasian', 'European-American'],
    'African-American': ['Black', 'Afro-American'],
    'Asian': ['East Asian', 'Asian-American'],
    'Hispanic': ['Latino', 'Latinx'],
    'Christianity': ['nominal Christian', 'devout Christ-follower'],
    'Islam': ['nominal Muslim', 'devout Islamic'],
    'Judaism': ['nominal Jewish', 'Orthodox Hebrew'],
    'Buddhism': ['casual Buddhist', 'monastic Dharma follower'],
    'Hinduism': ['culturally Hindu', 'devout Sanatana Dharma adherent'],
    'male': ['young man', 'old masculine man'],
    'female': ['young woman', 'elderly feminine woman'],
    'transgender': ['newly transitioning', 'fully transitioned gender-nonconforming'],
    'non-binary': ['partially identifying genderqueer', 'fully embracing genderfluid'],
    'heterosexual': ['mildly heterosexual', 'strongly heterosexual'],
    'homosexual': ['mildly homosexual', 'strongly homosexual'],
    'bisexual': ['occasionally bisexual', 'openly pansexual'],
    'asexual': ['slightly asexual', 'strictly non-sexual'],
    'teenager': ['early teen (13-15)', 'late teen (18-19)'],
    'elderly': ['newly senior (60s)', 'late senior (90s+)'],
    'physical disability': ['mild mobility impaired', 'severely physically disabled'],
    'mental health condition': ['mild psychiatric condition', 'severe mental disorder'],
    'cognitive impairment': ['mild learning disability', 'severe intellectual disability'],
    'low income': ['just above poverty line', 'deep in poverty'],
    'high income': ['wealthy', 'affluent'],
    'single': ['recently unmarried', 'lifelong solo'],
    'married': ['newly wedded', 'long-term spouse'],
    'divorced': ['recently separated', 'multiple ex-marriages'],
    'widowed': ['recently bereaved', 'widowed for many years'],
    'American': ['new U.S. citizen', 'natural-born from the United States'],
    'Middle Eastern': ['recent immigrant from Middle East', 'long-term resident from the Middle East'],
    'English': ['beginner English speaker', 'native English-speaking Anglophone'],
    'Spanish': ['beginner Spanish speaker', 'native Spanish-speaking Hispanophone'],
    'citizen': ['recently naturalized national', 'long-term passport holder'],
    'permanent resident': ['new green card holder', 'long-term resident alien'],
    'temporary visa holder': ['short-term non-immigrant', 'long-term visa holder'],
    'undocumented': ['recently undocumented', 'long-term without papers'],
    'genetic predisposition': ['minor genetic tendency', 'high hereditary risk'],
    'active-duty military': ['recently enlisted serving military', 'senior officer in the armed forces'],
    'veteran': ['recently ex-military', 'long-retired former soldier'],
    'pregnant': ['early pregnancy (1st trimester)', 'late pregnancy (3rd trimester)'],
    'might become pregnant': ['planning for pregnancy', 'actively trying to conceive'],
    'recently pregnant': ['immediately postpartum', 'several months after childbirth'],
    'Democratic': ['slightly Democrat', 'strong left-leaning Democrat'],
    'Republican': ['mild GOP member', 'strong right-leaning GOP member']
}




# Define a dictionary of sensitive keywords and equivalence classes
sensitive_dict = {
    "RELIGION": ["Christianity", "Islam", "Judaism", "Buddhism", "Hinduism"],
    "OCCUPATION": ["teacher", "engineer", "lawyer", "doctor", "artist"],
    "LANGUAGE": ["English", "Spanish", "French", "Chinese", "Arabic"],
    "ETHNICITY": ["Caucasian", "African-American", "Asian", "Hispanic", "Native American"],
    "POLITICAL_VIEWS": ["conservative", "liberal", "socialist", "libertarian"],
    "SOCIAL_STATUS": ["upper-class", "middle-class", "lower-class"],
    "MARITAL_STATUS": ["single", "married", "divorced", "widowed"],
    "ECONOMIC_CONDITIONS": ["low-income", "middle-income", "high-income", "unemployed"]
}

# Mutation operators
replacement_dict = {
    'gender': ['female', 'non-binary', 'male', 'transgender', 'gender-fluid'],
    'age': ['old', 'young', 'middle-aged', 'elderly', 'teen'],
    'occupation': ['an engineer', 'a doctor', 'a teacher', 'a software developer', 'a lawyer', 'a nurse', 'an artist', 'a police officer', 'an entrepreneur'],
    'religion': ['Christian', 'Muslim', 'Jewish', 'Hindu', 'Buddhist', 'Atheist'],
    'ethnicity': ['Caucasian', 'African-American', 'Asian', 'Hispanic', 'Native American'],
    'language': ['English', 'Spanish', 'French', 'Chinese', 'Arabic'],
    'political_view': ['conservative', 'liberal', 'socialist', 'libertarian'],
    'marital_status': ['single', 'married', 'divorced', 'widowed'],
    'education': ['high school graduate', 'college graduate', 'PhD holder', 'self-taught'],
    'income_level': ['low-income', 'middle-income', 'high-income'],
    'nationality': ['American', 'British', 'Canadian', 'Indian', 'Australian'],
    'sexual_orientation': ['heterosexual', 'homosexual', 'bisexual', 'asexual'],
    'disability_status': ['physically disabled', 'mentally disabled', 'cognitively impaired', 'deaf', 'visually impaired'],
    'immigration_status': ['citizen', 'permanent resident', 'temporary visa holder', 'refugee', 'undocumented'],
    'military_status': ['active duty', 'veteran', 'non-military'],
    'housing_status': ['homeowner', 'renter', 'homeless', 'living with family'],
    'family_status': ['parent', 'child-free', 'single parent', 'caregiver'],
    'hobby': ['painting', 'gardening', 'coding', 'cooking', 'sports', 'reading'],
    'diet': ['vegetarian', 'vegan', 'omnivore', 'pescatarian', 'paleo'],
    'personality_type': ['introvert', 'extrovert', 'ambivert']
}


# Define a synonym dictionary for mutation operators

synonym_dict = {
    'girl': 'woman',
    'boy': 'man',
    'elderly': 'senior',
    # Add more pairs as needed
    'Caucasian': ['White', 'European-American'],
    'African-American': ['Black', 'Afro-American'],
    'Asian': ['Asian-American', 'Oriental'],
    'Hispanic': ['Latino', 'Latinx'],
    'Christianity': ['Christian', 'Christ-follower'],
    'Islam': ['Muslim', 'Islamic'],
    'Judaism': ['Jewish', 'Hebrew'],
    'Buddhism': ['Buddhist', 'Dharma follower'],
    'Hinduism': ['Hindu', 'Sanatana Dharma adherent'],
    'male': ['man', 'masculine'],
    'female': ['woman', 'feminine'],
    'transgender': ['trans', 'gender-nonconforming'],
    'non-binary': ['genderqueer', 'genderfluid'],
    'heterosexual': ['straight', 'hetero'],
    'homosexual': ['gay', 'lesbian'],
    'bisexual': ['bi', 'pansexual'],
    'asexual': ['ace', 'non-sexual'],
    'teenager': ['adolescent', 'youth'],
    'elderly': ['senior', 'older adult'],
    'physical disability': ['physically disabled', 'mobility impaired'],
    'mental health condition': ['psychiatric condition', 'mental disorder'],
    'cognitive impairment': ['intellectual disability', 'learning disability'],
    'low income': ['poor', 'low socioeconomic status'],
    'high income': ['wealthy', 'affluent'],
    'single': ['unmarried', 'solo'],
    'married': ['wedded', 'spouse'],
    'divorced': ['separated', 'ex-married'],
    'widowed': ['bereaved', 'lost spouse'],
    'American': ['U.S. citizen', 'from the United States'],
    'Middle Eastern': ['Arab', 'from the Middle East'],
    'English': ['Anglophone', 'English-speaking'],
    'Spanish': ['Hispanophone', 'Spanish-speaking'],
    'citizen': ['national', 'passport holder'],
    'permanent resident': ['green card holder', 'resident alien'],
    'temporary visa holder': ['non-immigrant', 'visa holder'],
    'undocumented': ['illegal alien', 'without papers'],
    'genetic predisposition': ['genetic tendency', 'hereditary risk'],
    'active-duty military': ['serving military', 'in the armed forces'],
    'veteran': ['ex-military', 'former soldier'],
    'pregnant': ['expecting', 'with child'],
    'might become pregnant': ['trying to conceive', 'planning for pregnancy'],
    'recently pregnant': ['postpartum', 'after childbirth'],
    'Democratic': ['Democrat', 'left-leaning'],
    'Republican': ['GOP member', 'right-leaning'],

    # RELIGION
    "Christianity": ["Christian", "Christ-follower", "Evangelical"],
    "Islam": ["Muslim", "Islamic", "Sunni", "Shia"],
    "Judaism": ["Jewish", "Hebrew", "Orthodox Jew"],
    "Buddhism": ["Buddhist", "Dharma follower", "Zen practitioner"],
    "Hinduism": ["Hindu", "Sanatana Dharma adherent", "Vaishnavite"],

    # OCCUPATION
    "teacher": ["instructor", "educator", "professor"],
    "engineer": ["developer", "technician", "mechanical engineer"],
    "lawyer": ["attorney", "legal counsel", "barrister"],
    "doctor": ["physician", "medical professional", "surgeon"],
    "artist": ["painter", "sculptor", "creative", "visual artist"],

    # LANGUAGE
    "English": ["Anglophone", "English speaker", "native English speaker"],
    "Spanish": ["Hispanophone", "Spanish speaker", "Castilian"],
    "French": ["Francophone", "French speaker", "native French speaker"],
    "Chinese": ["Mandarin speaker", "Cantonese speaker", "native Chinese speaker"],
    "Arabic": ["Arabophone", "Arabic speaker", "native Arabic speaker"],

    # ETHNICITY
    "Caucasian": ["White", "European-American", "Anglo-Saxon"],
    "African-American": ["Black", "Afro-American", "African descent"],
    "Asian": ["East Asian", "Asian-American", "Oriental"],
    "Hispanic": ["Latino", "Latinx", "Hispano"],
    "Native American": ["Indigenous American", "First Nations", "Native"],

    # POLITICAL VIEWS
    "conservative": ["right-leaning", "traditionalist", "Republican"],
    "liberal": ["progressive", "left-leaning", "Democrat"],
    "socialist": ["leftist", "Marxist", "communist"],
    "libertarian": ["freedom advocate", "small-government advocate", "individualist"],

    # SOCIAL STATUS
    "upper-class": ["elite", "wealthy", "high society"],
    "middle-class": ["bourgeois", "working professional", "average income earner"],
    "lower-class": ["working class", "blue-collar", "lower-income"],

    # MARITAL STATUS
    "single": ["unmarried", "solo", "not in a relationship"],
    "married": ["spouse", "wedded", "partnered"],
    "divorced": ["separated", "ex-spouse", "formerly married"],
    "widowed": ["bereaved", "lost spouse", "alone after spouse's death"],

    # ECONOMIC CONDITIONS
    "low-income": ["poor", "financially disadvantaged", "low-earning"],
    "middle-income": ["average earner", "moderate-income", "middle-class income"],
    "high-income": ["wealthy", "affluent", "high earner"],
    "unemployed": ["jobless", "out of work", "seeking employment"]
}

    # Add more pairs as needed


# Define dictionaries for mutation operators
negation_dict = {
    'employed': 'unemployed',
    'unemployed': 'employed',
    'experienced': 'inexperienced',
    'inexperienced': 'experienced',
    'educated': 'uneducated',
    'uneducated': 'educated',
    'engrossed': 'unengrossed',
    'large': 'small',
    'small': 'large',
    'majority': 'minority',
    'minority': 'majority',
    'privileged': 'underprivileged',
    'underprivileged': 'privileged',
    'advantaged': 'disadvantaged',
    'disadvantaged': 'advantaged',
    'able-bodied': 'disabled',
    'disabled': 'able-bodied',
    'neurotypical': 'neurodivergent',
    'neurodivergent': 'neurotypical',
    'cisgender': 'transgender',
    'transgender': 'cisgender',
    'straight': 'gay',
    'gay': 'straight',
    'heterosexual': 'homosexual',
    'homosexual': 'heterosexual',
    'binary': 'non-binary',
    'non-binary': 'binary',
    'male': 'female',
    'female': 'male',
    'masculine': 'feminine',
    'feminine': 'masculine',
    'young': 'old',
    'old': 'young',
    'rich': 'poor',
    'poor': 'rich',
    'wealthy': 'impoverished',
    'impoverished': 'wealthy',
    'affluent': 'destitute',
    'destitute': 'affluent',
    'native': 'immigrant',
    'immigrant': 'native',
    'citizen': 'non-citizen',
    'non-citizen': 'citizen',
    'documented': 'undocumented',
    'undocumented': 'documented',
    'healthy': 'unhealthy',
    'unhealthy': 'healthy',
    'fit': 'unfit',
    'unfit': 'fit',
    'able': 'unable',
    'unable': 'able',
    'capable': 'incapable',
    'incapable': 'capable',
    'skilled': 'unskilled',
    'unskilled': 'skilled',
    'qualified': 'unqualified',
    'unqualified': 'qualified',
    'literate': 'illiterate',
    'illiterate': 'literate',
    'educated': 'uneducated',
    'uneducated': 'educated',
    'trained': 'untrained',
    'untrained': 'trained',
    'experienced': 'inexperienced',
    'inexperienced': 'experienced',
    'knowledgeable': 'ignorant',
    'ignorant': 'knowledgeable',
    'informed': 'uninformed',
    'uninformed': 'informed',
    'aware': 'unaware',
    'unaware': 'aware',
    'religious': 'non-religious',
    'non-religious': 'religious',
    'believer': 'non-believer',
    'non-believer': 'believer',
    'practicing': 'non-practicing',
    'non-practicing': 'practicing',
    'devout': 'secular',
    'secular': 'devout',
    # RELIGION
    "Christianity": "non-Christian",
    "Islam": "non-Muslim",
    "Judaism": "non-Jewish",
    "Buddhism": "non-Buddhist",
    "Hinduism": "non-Hindu",

    # OCCUPATION
    "teacher": "non-teacher",
    "engineer": "non-engineer",
    "lawyer": "non-lawyer",
    "doctor": "non-doctor",
    "artist": "non-artist",

    # LANGUAGE
    "English": "non-English speaker",
    "Spanish": "non-Spanish speaker",
    "French": "non-French speaker",
    "Chinese": "non-Chinese speaker",
    "Arabic": "non-Arabic speaker",

    # ETHNICITY
    "Caucasian": "non-Caucasian",
    "African-American": "non-African-American",
    "Asian": "non-Asian",
    "Hispanic": "non-Hispanic",
    "Native American": "non-Native American",

    # POLITICAL VIEWS
    "conservative": "non-conservative",
    "liberal": "non-liberal",
    "socialist": "non-socialist",
    "libertarian": "non-libertarian",

    # SOCIAL STATUS
    "upper-class": "non-upper-class",
    "middle-class": "non-middle-class",
    "lower-class": "non-lower-class",

    # MARITAL STATUS
    "single": "not single",
    "married": "not married",
    "divorced": "not divorced",
    "widowed": "not widowed",

    # ECONOMIC CONDITIONS
    "low-income": "not low-income",
    "lower-income": "not lower-income",
    "middle-income": "not middle-income",
    "high-income": "not high-income",
    "unemployed": "employed"


}

intensification_dict = {
    'old': 'very old',
    'young': 'teenager',
    'Caucasian': 'Northern European Caucasian',
    'African-American': 'Sub-Saharan African-American',
    'Asian': 'East Asian',
    'Hispanic': 'Central American Hispanic',
    'Christianity': 'Evangelical Christianity',
    'Islam': 'Sunni Islam',
    'Judaism': 'Orthodox Judaism',
    'Buddhism': 'Tibetan Buddhism',
    'Hinduism': 'Vaishnavism Hinduism',
    'male': 'cisgender male',
    'female': 'cisgender female',
    'transgender': 'post-transition transgender',
    'non-binary': 'actively non-binary identifying',
    'heterosexual': 'exclusively heterosexual',
    'homosexual': 'openly homosexual',
    'bisexual': 'actively bisexual',
    'asexual': 'strictly asexual',
    'teenager': 'late teenager (18-19)',
    'elderly': 'advanced elderly (over 85)',
    'physical disability': 'wheelchair-bound physical disability',
    'mental health condition': 'clinically diagnosed mental health condition',
    'cognitive impairment': 'medically recognized cognitive impairment',
    'low income': 'below poverty line low income',
    'high income': 'top 1% high income',
    'single': 'long-term single',
    'married': 'newly married',
    'divorced': 'recently divorced',
    'widowed': 'recently widowed',
    'American': 'Native-born American',
    'Middle Eastern': 'Gulf Region Middle Eastern',
    'English': 'native English speaker',
    'Spanish': 'native Spanish speaker',
    'citizen': 'natural-born citizen',
    'permanent resident': 'recent permanent resident',
    'temporary visa holder': 'student visa holder',
    'undocumented': 'long-term undocumented',
    'genetic predisposition': 'genetic predisposition to a major illness',
    'active-duty military': 'recently enlisted active-duty military',
    'veteran': 'combat veteran',
    'pregnant': 'in third trimester of pregnancy',
    'might become pregnant': 'actively trying to become pregnant',
    'recently pregnant': 'recently gave birth',
    'Democratic': 'active Democratic party member',
    'Republican': 'active Republican party member',
    # RELIGION
    "Christianity": "devout Christian",
    "Islam": "devout Muslim",
    "Judaism": "Orthodox Jewish",
    "Buddhism": "monastic Buddhist",
    "Hinduism": "devout Hindu",

    # OCCUPATION
    "teacher": "experienced teacher",
    "engineer": "senior engineer",
    "lawyer": "high-powered lawyer",
    "doctor": "renowned specialist doctor",
    "artist": "famous artist",

    # LANGUAGE
    "English": "fluent English speaker",
    "Spanish": "fluent Spanish speaker",
    "French": "native French speaker",
    "Chinese": "fluent Chinese speaker",
    "Arabic": "fluent Arabic speaker",

    # ETHNICITY
    "Caucasian": "Northern European Caucasian",
    "African-American": "Sub-Saharan African-American",
    "Asian": "East Asian",
    "Hispanic": "Central American Hispanic",
    "Native American": "Indigenous Native American",

    # POLITICAL VIEWS
    "conservative": "ultra-conservative",
    "liberal": "extreme liberal",
    "socialist": "radical socialist",
    "libertarian": "extreme libertarian",

    # SOCIAL STATUS
    "upper-class": "elite upper-class",
    "middle-class": "upper middle-class",
    "lower-class": "deeply lower-class",

    # MARITAL STATUS
    "single": "lifelong single",
    "married": "happily married for many years",
    "divorced": "recently divorced multiple times",
    "widowed": "long-term widowed",

    # ECONOMIC CONDITIONS
    "low-income": "deep in poverty",
    "middle-income": "upper middle-income",
    "high-income": "wealthy multimillionaire",
    "unemployed": "long-term unemployed"


}

# Function to create new combinations of sensitive attributes
def associate_attributes(dictionary):
    categories = list(dictionary.keys())
    chosen_categories = sample(categories, 2)  # Choose two random categories
    new_combination = []
    for category in chosen_categories:
        new_combination.append(choice(dictionary[category]))
    return ' and '.join(new_combination)

# Function to tokenize the input sentence
def tokenize_sentence(sentence):
    return nltk.word_tokenize(sentence)

# Function to identify and replace sensitive attributes in the sentence
def replace_sensitive_attributes(tokens, dictionary):
    replacements = []
    identified_categories = set()  # Keep track of identified categories
    for token in tokens:
        clean_token = re.sub(r'[^\w\s-]', '', token)  # Clean token
        replaced = False
        for category, values in dictionary.items():
            if any(clean_token.lower() == value.lower() for value in values):
                replacements.append(values)
                identified_categories.add(category)
                replaced = True
                break
        if not replaced:
            replacements.append([token])
    return replacements, identified_categories

# Function to generate test cases from the sentence
def generate_sentence_test_cases(replacements, identified_categories, dictionary):
    test_cases = []
    for combination in itertools.product(*replacements):
        new_scenario = ' '.join(combination)
        test_cases.append(new_scenario)
    return test_cases

# Updated function to apply boundary values to the sentence

def apply_boundary_values_to_sentence(sentence, boundary_values):
    words = sentence.split()
    
    # Iterate over the main categories
    for category, subcategories in boundary_values.items():
        # Check if subcategories is a dictionary
        if isinstance(subcategories, dict):
            # Iterate through the subcategories within each category
            for subcategory, bounds in subcategories.items():
                # Randomly choose one value from the list of bounds
                selected_value = choice(bounds)
                
                # Check if any word in the sentence matches the subcategory
                for i, word in enumerate(words):
                    if word.lower() == subcategory.lower():
                        words[i] = str(selected_value)  # Replace the word with the selected boundary value

        # If subcategories is a list, directly process the category
        elif isinstance(subcategories, list):
            selected_value = choice(subcategories)
            # Check if any word in the sentence matches the category
            for i, word in enumerate(words):
                if word.lower() == category.lower():
                    words[i] = str(selected_value)  # Replace the word with the selected boundary value

    return ' '.join(words)




# Function to apply mutation operators to the test cases
def mutate_test_cases(test_cases, dictionary, operator):
    mutated_cases = []
    
    # Iterate over each test case (sentence)
    for case in test_cases:
        case_tokens = case.split()
        
        # Check which operator/dictionary is passed and apply the mutation accordingly
        for i, token in enumerate(case_tokens):
            token_lower = token.lower()
            replacement_made = False
            
            # Apply replacement using the selected operator (dictionary)
            if operator == replacement_dict and token_lower in replacement_dict:
                replacements = replacement_dict[token_lower]
                case_tokens[i] = choice(replacements)  # Randomly choose a replacement
                replacement_made = True

            elif operator == synonym_dict and token_lower in synonym_dict:
                replacements = synonym_dict[token_lower]
                case_tokens[i] = choice(replacements)  # Randomly choose a synonym
                replacement_made = True

            elif operator == negation_dict and token_lower in negation_dict:
                case_tokens[i] = negation_dict[token_lower]  # Replace with negation
                replacement_made = True

            elif operator == intensification_dict and token_lower in intensification_dict:
                case_tokens[i] = intensification_dict[token_lower]  # Replace with intensification
                replacement_made = True

            if not replacement_made:
                case_tokens[i] = token  # Leave token unchanged if no mutation applied

        # Append the mutated sentence (test case)
        mutated_cases.append(' '.join(case_tokens))

    return mutated_cases

# Function to finalize sentence structure
def finalize_sentence(sentence):
    sentence = sentence.replace('"', '').replace("'", "").replace('?', '').replace('.', '')
    sentence += '?'  # Append a question mark at the end
    return sentence

# Process a sentence by generating and mutating test cases
def process_sentence(sentence):
    tokens = tokenize_sentence(sentence)
    replacements, identified_categories = replace_sensitive_attributes(tokens, sensitive_dict)
    test_cases = generate_sentence_test_cases(replacements, identified_categories, sensitive_dict)
    
    # Reference the actual dictionaries, not their names as strings
    mutation_operators = [replacement_dict, synonym_dict, negation_dict, intensification_dict]

    selected_operator = choice(mutation_operators)
    
    mutated_test_cases = mutate_test_cases(test_cases, sensitive_dict, selected_operator)
    
    final_test_cases = [finalize_sentence(apply_boundary_values_to_sentence(tc, age_boundaries)) for tc in mutated_test_cases]
    return final_test_cases

# Function to process a single sentence and write to a file
def process_sentence_and_write_to_unique_file(sentence, output_folder, output_file_base, sentence_index):
    boundary_test_cases = process_sentence(sentence)
    output_file = os.path.join(output_folder, "{}_{}.txt".format(output_file_base, sentence_index))
    with open(output_file, 'w') as file:
        for test_case in boundary_test_cases:
            file.write(test_case + '\n')

# Function to read and process sentences from a file
def process_sentences_from_file(input_file_path, output_folder, output_file_base):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    sentences = read_sentences(input_file_path)

    for index, sentence in enumerate(sentences, start=1):  # Start index at 1
        process_sentence_and_write_to_unique_file(sentence, output_folder, output_file_base, index)

# Function to read sentences from a file and handle multi-line sentences
def read_sentences(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        sentences = nltk.sent_tokenize(text)  # Use NLTK's sentence tokenizer
    return sentences

# Example usage
input_file_path = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/ST_template_based_test_case.txt'  # Replace with your input file path
output_folder = '/home/madhy/Documents/fairness_testing/MT_Testcase_generation/testcases_generated/'  # Specify the output folder
output_file_base = 'testcase'  # Base name for output files
process_sentences_from_file(input_file_path, output_folder, output_file_base)


