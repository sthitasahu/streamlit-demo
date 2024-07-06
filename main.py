from dotenv import load_dotenv # type: ignore
load_dotenv()
import streamlit as st # type: ignore
import google.generativeai as genai # type: ignore
import os


genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')


def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text


st.set_page_config(page_title="Q & A demo")
st.title("Gemini Pro Interaction")
input=st.text_input("Input :" ,key="input")
submit=st.button("Ask me a question")

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is:")
    st.write(response)


