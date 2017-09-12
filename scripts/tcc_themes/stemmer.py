import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
import html

cachedStopWords = stopwords.words("english")
regex_code = re.compile(r'<code>[^<]*<\/code>')
regex_tags = re.compile(r'(<!--.*?-->|<[^>]*>)')
regex_white_space = re.compile(r'\s+')
regex_only_letters = re.compile(r'^[^_\d\W]+$')
tokenizer = RegexpTokenizer(r'\w+')
stemmer = SnowballStemmer("english")

def process_text (text):
    text = regex_code.sub('', text)
    text = regex_tags.sub('', text)
    text = html.unescape(text)
    text = regex_white_space.sub(" ", text)
    text = ' '.join(tokenizer.tokenize(text))
    text = ' '.join([word for word in text.split() if word.lower() not in cachedStopWords])
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    text = ' '.join([word for word in text.split() if regex_only_letters.match(word)])
    return text