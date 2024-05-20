import pandas as pd
import streamlit as st
import joblib
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
all_stopwords=stopwords.words('english')
import re

with open('Customer_comments.pkl', 'rb') as f:
    model = joblib.load(f)

st.title('This is customer comments based prediction ')
customer_comments=st.header('Hotel Review')

st.text_area('Enter your comments')
button=st.button('Enter')

def pre_processing(text):
    tokenizer=nltk.word_tokenize(text)
    processed_text= [i for i in text.split() if i.isalpha and i not in all_stopwords]
    processed_text=[i for i in processed_text if len(i) > 3]
    processed_text= [ps.stem(i) for i in processed_text]
    revised_data=' '.join(processed_text)
    revised_data = re.sub(r'[^a-zA-Z0-9\s]', '', revised_data)
    return revised_data

if button:
    processed_text=pre_processing(str(customer_comments))
    result=model.predict([processed_text])
    result=result[0]

    if result > 3:
        st.write('The hotel have good review')
    else:
        st.write('The hotel have Negative review')

    
