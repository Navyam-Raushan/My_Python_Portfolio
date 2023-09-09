import streamlit as st
from send_email import send_mail

st.title("Contact Us")

with st.form(key="email_form"):
    sender_mail_id = st.text_input("Enter your email id")
    raw_message = st.text_area("Enter your message")

    # We need formatted message to see all details
    # we must add a break line after subject and "\"

    message = f"""\
Subject: New email from {sender_mail_id}

From: {sender_mail_id}
{raw_message}

"""
    # message = message + "\n" + sender_mail_id
    button = st.form_submit_button("Submit")

    # The button will only be executed if it's pressed as it takes true.
    if button:
        send_mail(message)
        st.info("Your Email send Successfully.")
