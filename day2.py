import streamlit as st
from langchain.llms import openai
from langchain.llms import OpenAI
import os

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

st.title('my first gen AI app V2')

st.markdown("""
this is a sample markdown
try it on your 'own'
""")

#openai_api_key = st.sidebar.text_input("open AI key")
hf_key = st.sidebar.text_input("Hugging Face key")
#name = st.text_input("enter some text", "enter here")
#option = st.radio("choose one option:", options = ["Option1", "Option2"], index=0)

value = st.slider("Temperature value: ", 0.0, 2.0, 1.0, step=0.1)
print(value)
#print(value)
#print(option)

def gen_response(txt):
    #llm = OpenAI(temperature = 0.7, openai_api_key=openai_api_key)
    llm = HuggingFaceEndpoint( \
    # repo_id="huggingfaceh4/zephyr-7b-alpha",  # 7B model on mistral
    repo_id="microsoft/Phi-3-mini-4k-instruct",  #3.8B model
    #temperature= value,
    huggingfacehub_api_token= hf_key,
    )
    st.info(llm(txt))

with st.form("sample app"):
    txt = st.text_area("enter text:", "what GPT stands for")
    subm = st.form_submit_button("submit")
    if subm:
        gen_response(txt)


