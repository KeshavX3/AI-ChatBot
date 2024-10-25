from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question) -> None:
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Lakshmi Chit Fund AI")
st.header("Ask Me Anything")
input = st.text_input("Input: " , key = "input")
submit = st.button("Ask")


if submit :
    response = get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)