from langchain.llms import OpenAI
from dotenv import load_dotenv
import os  # Import the os module

load_dotenv()

import streamlit as st


# Function to interact with the OpenAI model
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="text-davanchi-003", temperature=0.5)  # Corrected typo in temperature
    response = llm.predict(question)  # Corrected variable name
    return response

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")
input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_openai_response(input_text)
    st.subheader("The response is:")
    st.write(response)

