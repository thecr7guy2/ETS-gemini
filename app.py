import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import PyPDF2 as pdf
import json

load_dotenv("../.env")
gemini_api_key = os.getenv('GEMINI_PRO_API_KEY')
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel("gemini-pro")

print("sai")

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

input_prompt="""

resume:{text}
description:{jd}

Imagine you are an advanced Application Tracking System (ATS). Your goal is to tailor resumes for the competitive tech industry, specializing in software engineering, data science, data analysis, big data engineering and machine learning engineer roles. You deeply analyze the resume against specific job description, understanding nuances in tech skills, project experiences, and educational backgrounds. you offer comprehensive feedback, highlighting strengths and pinpointing gaps with recommendations for improvement. your final answer which you will output in the form of a json will will include a percentage match to the job description, detailed missing keywords crucial for the role, and a comprehensive feedback, highlighting strengths and pinpointing gaps with recommendations for improvement to guide applicants on enhancing their resumes for better alignment with desired job roles. z



"""

st.set_page_config(page_title = "ETS-Gemini")

st.header("ETS-Gemini : Improve Your Resume")

jd=st.text_area("Paste the Job Description")

uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        print(response)
        print(response[1:])
        # data = json.loads(response)
        # st.header("Match Percentage")
        # st.metric(label="Match Percentage", value=f"{data['match_percentage']}%")
        st.subheader(response)


