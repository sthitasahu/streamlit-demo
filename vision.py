from PIL import Image # type: ignore
from dotenv import load_dotenv # type: ignore
load_dotenv()
import streamlit as st # type: ignore
import google.generativeai as genai # type: ignore
import os


genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro-vision')


def get_gemini_response(prompt, image):
    if(prompt !=" "):
     response = model.generate_content([prompt,image])
    else :
     response=model.generate_content(image)

    return response.text


st.set_page_config(page_title="Q & A demo")
st.title("Gemini Pro Vision Interaction")
input=st.text_input("Input :" ,key="input")
submit=st.button("Ask me a question")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

submit=st.button("Tell me about the image")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The response is:")
    st.write(response)


