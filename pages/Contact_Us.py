import streamlit as st

st.title("Contact Us")

with st.form(key="my_form"):
    mail_id = st.text_input("Enter your email I'D")
    message = st.text_area("Enter your message")
    button = st.form_submit_button("Submit")

    # The button will only be executed if it's pressed as it takes true.
    if button:
        print("I am pressed.")
