
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="My ML App",
    page_icon="🤖",
    layout="centered"
)

# App Title
st.title("🤖 My Machine Learning App")

# Description
st.write("Welcome to my simple Streamlit application!")

# Text Input
user_text = st.text_input("Enter your text:")

# Display Entered Text
if user_text:
    st.success("You entered:")
    st.write(user_text)
else:
    st.info("Please enter some text above.")

# Footer
st.markdown("---")
st.write("Created by: Saniya Yerudkar")
