import streamlit as st
from agents import smart_router

st.title("TASKSENSE")

user_input = st.text_area("Enter your input")

if st.button("Run"):
    with st.spinner("Thinking..."):
        output = smart_router(user_input)
        st.write(output)
