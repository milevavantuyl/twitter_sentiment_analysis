import pickle 
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import re

################# File Input/ Output Operations #################
def save_object(obj, path): 
    "Save an object in a pickle file at the specified path"
    with open(path, 'wb') as file: 
        pickle.dump(obj, file)
        
################# Data Cleaning and Processing #################

def data_cleaning(texts): 
    """  """
    remove_stop_words = False #TODO set as param
    lemmatizer=WordNetLemmatizer()
    tokenizer=TweetTokenizer()
    clean_text=[]
    for text in texts: 
        text = text.lower() #lowe case
        text = re.sub("\s\s+", " ", text) #remove extra spaces
        text = text.encode('ascii',errors='ignore').decode() #Remove non-ASCII characters
        text = re.sub(r'[0-9]', '', text) #Remove numbers
        lemmatized_tokens=[]
        tokens=tokenizer.tokenize(text.lower())
        for token in tokens:    
            lemmatized_token=lemmatizer.lemmatize(token)
            if remove_stop_words:
                if lemmatized_token not in stopwords.words('english'): lemmatized_tokens.append(lemmatized_token) 
            else: 
                lemmatized_tokens.append(lemmatized_token)
        clean_text.append(' '.join(lemmatized_tokens))
    return clean_text