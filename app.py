import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from PIL import Image
import google.generativeai as genai

# ----------------------------
# Configure API Key and Load Model
# ----------------------------
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# ----------------------------
# Streamlit Front-End
# ----------------------------
st.set_page_config(page_title="Image to Text App", layout="centered")
st.header("🎯 Image to Text: Build a Digital Marketing Campaign", divider="green")

# User Input Fields
prompt = st.text_input("📝 Enter your prompt")
uploaded_image = st.file_uploader("📤 Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

# Preview Uploaded Image
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="🖼️ Uploaded Image", use_container_width=True)

# ----------------------------
# Core Function for Image-to-Text Generation
# ----------------------------
def process_img(prompt, image):
    if prompt !="":
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content([prompt])
    return response.text

# Run the Function
submit = st.button("Submit")

if submit :
    response = process_img(prompt,image)
    st.subheader(":orange[Response:]")
    st.markdown(response)
