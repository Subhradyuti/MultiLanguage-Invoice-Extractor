from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input_text, image, prompt):
    response = model.generate_content([
        {"text": input_text},
        image,
        {"text": prompt}
    ])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = {
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

# Initialize our Streamlit app
st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.header("MultiLanguage Invoice Extractor")
st.text_input("Input Prompt: ", key="input")
upload_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
submit = st.button("Tell Me About The Invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload an image as an invoice and you
will have to answer any questions based on the uploaded invoice image.
"""

# If submit button is clicked
if submit:
    image_data = input_image_details(upload_file)
    response = get_gemini_response(input_prompt, image_data, st.session_state.input)
    st.subheader("The Response is")
    st.write(response)
