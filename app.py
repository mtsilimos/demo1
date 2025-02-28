import jwt
import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


import jwt
payload = {
 "username": "john_doe",
 "role": "user",
 
}


token = jwt.encode(payload, 'AID', algorithm='HS256')

    
if st.button("Validate"):
    payload = jwt.decode(token, 'AID', algorithms=['HS256'])
    st.write("You are authorized to use the app")
        
    st.write("Role:", payload['role'])
    qa = pipeline("question-answering", model="deepset/roberta-base-squad2")
    text = st.text_area("text")
    question = st.text_input("question")
    if st.button("Get Answer"):
        answer = qa(question, text)
        st.write("Answer:", answer['answer'])
        st.write("Score:", answer['score'] * 100)
