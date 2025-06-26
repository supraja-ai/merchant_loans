import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenize & lowercase
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english')]
    return filtered_tokens

# Test text processing
print(preprocess_text("Hello! How can I help you today?"))
