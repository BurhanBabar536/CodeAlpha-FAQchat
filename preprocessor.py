import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Remove punctuation and special characters
    text = re.sub(r'[^a-z0-9\s]', '', text)

    # Step 3: Tokenize (split into words)
    tokens = nltk.word_tokenize(text)

    # Step 4: Remove stopwords (e.g. "the", "is", "a")
    tokens = [t for t in tokens if t not in stop_words]

    # Step 5: Lemmatize (e.g. "running" -> "run")
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return ' '.join(tokens)