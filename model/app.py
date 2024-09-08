import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizerUpdated.pkl','rb'))
model = pickle.load(open('modelUpdated.pkl','rb'))

st.header('Public Sentiment Analysis', divider='red')


#selected3 = option_menu(None, ["Home", "Identity Detection", "Banking Usecase", "Text Scam" ,"Dating Usecase","Reporting", 'Team'], 
 #   icons=['house', 'cloud-upload', "list-task", "list-task","list-task",'gear'], 
  #  menu_icon="cast", default_index=0, orientation="horizontal",
   # styles={
    #    "container": {"padding": "0!important", "background-color": "#fafafa"},
      #  "icon": {"color": "orange", "font-size": "15px"}, 
       # "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        #"nav-link-selected": {"background-color": "green"},
    #})



def identity_scam():
    tfidf = pickle.load(open('vectorizerUpdated.pkl','rb'))
    model = pickle.load(open('modelUpdated.pkl','rb'))

    input_sms = st.text_area("Enter the message")

    if st.button('Predict'):

        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = tfidf.transform([transformed_sms])
        # 3. predict
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 0:
            st.header("Negative Review !!")
        elif result == 1:
            st.header("Neutral !!")
        else:
            st.header("Positive Review !!")

    # Define your content for each tile
    
    #st.markdown("<center><b><span style='font-size: 30px;'>Katch is the platform designed for the identification and prevention of fraudulent activities.<center><b><span style='font-size: 24px;'>")

    #st.markdown("<center><span style='font-size: 20px;'>Katch is the platform designed for the identification and prevention of fraudulent activities.<center><span style='font-size: 20px;'>", unsafe_allow_html=True)


identity_scam()


    