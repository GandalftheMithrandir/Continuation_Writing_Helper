import streamlit as st
from utils import rater, feedback, compare, assist, pro_model


st.header("Continuation Writing Helper")
with st.sidebar:
    api_key = st.text_input("Please enter OpenAI api-key", type="password")
    st.markdown("[Get OpenAI api-key](https://platform.openai.com/account/api-keys)")
helper = st.selectbox("Please choose the help you wish to get from AI.", ["Rating", "Feedback and Suggestions", "Comparing the Revised and the Original Version", "Assistance for Pre-writing planning", "Providing Model Text"])
if helper == "Rating":
    text = st.text_input("Please input the text here.")
    guide = st.text_input("Please input the guiding sentences here.")
    learner_work = st.text_input("Please enter your completed work here.")

    role = st.selectbox("Please choose the role you wish AI would be.", ["High-School English teacher", "NMET rater"])
    if role == "High-School English teacher":
        way = st.selectbox("Please choose the way of rating", ["Holistic", "Analytical"])
    else:
        way = st.selectbox("Please choose the way of rating", ["Holistic", "Analytical"])

    submit = st.button("Generate")

    if submit and not api_key:
        st.info("OpenAI api-key can't be empty!")
        st.stop()
    if submit and not text:
        st.info("Text can't be empty!")
        st.stop()
    if submit and not guide:
        st.info("Guiding sentences can't be empty!")
        st.stop()
    if submit and not learner_work:
        st.info("Your work can't be empty!")
        st.stop()
    if submit:
        with st.spinner("AI is working...Please wait a second."):
            result = rater(api_key, role, way, text, guide, learner_work)
        st.divider()
        st.write(result)
elif helper == "Feedback and Suggestions":
    text = st.text_input("Please input the text here.")
    guide = st.text_input("Please input the guiding sentences here.")
    learner_work = st.text_input("Please enter your completed work here.")

    dim = st.selectbox("Please choose the dimensions you want AI to give feedback and suggestions.", ["ALL", "Content and Logical Coherence", "Vocabulary and Grammar", "Organization and Cohesion"])
    submit = st.button("Generate")

    if submit and not api_key:
        st.info("OpenAI api-key can't be empty!")
        st.stop()
    if submit and not text:
        st.info("Text can't be empty!")
        st.stop()
    if submit and not guide:
        st.info("Guiding sentences can't be empty!")
        st.stop()
    if submit and not learner_work:
        st.info("Your work can't be empty!")
        st.stop()
    if submit:
        with st.spinner("AI is working...Please wait a second."):
            result = feedback(api_key, dim, text, guide, learner_work)
        st.divider()
        st.write(result)
elif helper == "Comparing the Revised and the Original Version":
    text = st.text_input("Please input the text here.")
    guide = st.text_input("Please input the guiding sentences here.")
    original_version = st.text_input("Please input your original version here.")
    revised_version = st.text_input("Please input your revised version here.")
    submit = st.button("Generate")

    if submit and not api_key:
        st.info("OpenAI api-key can't be empty!")
        st.stop()
    if submit and not text:
        st.info("Text can't be empty!")
        st.stop()
    if submit and not guide:
        st.info("Guiding sentences can't be empty!")
        st.stop()
    if submit and not original_version:
        st.info("Original version can't be empty!")
        st.stop()
    if submit and not original_version:
        st.info("Revised version can't be empty!")
        st.stop()
    if submit:
        with st.spinner("AI is working...Please wait a second."):
            result = compare(api_key, text, guide, original_version, revised_version)
        st.divider()
        st.write(result)
elif helper == "Assistance for Pre-writing planning":
    text = st.text_input("Please input the text here.")
    guide = st.text_input("Please input the guiding sentences here.")
    submit = st.button("Generate")

    if submit and not api_key:
        st.info("OpenAI api-key can't be empty!")
        st.stop()
    if submit and not text:
        st.info("Text can't be empty!")
        st.stop()
    if submit and not guide:
        st.info("Guide can't be empty!")
        st.stop()
    if submit:
        with st.spinner("AI is working...Please wait a second."):
            result = assist(api_key, text, guide)
        st.divider()
        st.write(result)
elif helper == "Providing Model Text":
    text = st.text_input("Please input the text here.")
    guide = st.text_input("Please input the guiding sentences here.")
    submit = st.button("Generate")

    if submit and not api_key:
        st.info("OpenAI api-key can't be empty!")
        st.stop()
    if submit and not text:
        st.info("Text can't be empty!")
        st.stop()
    if submit and not guide:
        st.info("Guiding sentences can't be empty!")
        st.stop()
    if submit:
        with st.spinner("AI is working...Please wait a second."):
            result = pro_model(api_key, text, guide)
        st.divider()
        st.write(result)
