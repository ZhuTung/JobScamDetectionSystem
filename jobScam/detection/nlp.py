import nltk
import re, string
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import RegexpTokenizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

tokenizer = RegexpTokenizer(r'\w+')
stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def format_textarea(text):
    text = text.split('\n')
    text = ' '.join(text)

    return text

def clean_text(input):
    text = input.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    
    return text

def remove_stop_words(input):
    words = [w for w in input if w not in stop_words]
    return words

def combine_text(texts):
    combined_text = ' '.join(texts)
    return combined_text

def get_pos_tag(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    
def lemmatize_sentence(sentence):
    pos_tags = pos_tag(nltk.word_tokenize(sentence))
    lemmatized_sentence = []
    for word, tag in pos_tags:
        pos = get_pos_tag(tag)
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos=pos))
        
    return lemmatized_sentence

def process_text(text):
    text = clean_text(text)
    text = tokenizer.tokenize(text)
    text = remove_stop_words(text)
    text = combine_text(text)
    text = lemmatize_sentence(text)
    text = combine_text(text)
    
    return text