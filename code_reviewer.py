"""Importing required packages"""
! pip install streamlit
! pip install google-generativeai
#Streamlit package
import streamlit as st

#Google generative ai package
import google.generativeai as gai

#Setting up the google ai Api key
gai.configure(api_key="AIzaSyDxnP5VMe3fs932Fq77M1wu0sWu5XvDlbs")


#User Interface
st.title("An :blue[AI] _Code Reviewer_")
st.image("Botty.jpg")

st.subheader("Submit your Python code below, and I'll let you know if you are good to go!")
st.markdown("Kindly paste your Python code here")

user_prompt=st.text_area("Drop the code", placeholder="Paste your Python code here")

button_click=st.button("Submit Code")

if button_click:
    #instantiate the LLM model with a system prompt
    sys_prompt="""You are a helpful AI Python Code Reviewer. Users will submit their Python code.  You are expected to review and give receive feedback on potential bugs along with suggestions for fixes. Make sure that you analyze the submitted code and identify potential bugs, errors, or areas of improvement and present them to the user then you also provide the fixed code snippets with explanation. If the submitted code does not have any bugs, check for proper alternative code style the code and present it to the user. If the code is perfect in terms of style and it also does not contain any bugs then comment to the user that no bug fixes are required.
    No need to correct minor typographical errors inside a string used inside the print functions.
    In case, if a student asks any question outside of python code reviewing scope, politely decline and ask for a python code snippet only"""
    model=gai.GenerativeModel(model_name="gemini-1.5-flash",system_instruction=sys_prompt)

    #Give out the response
    response = model.generate_content(user_prompt)
    st.write(response.text)



