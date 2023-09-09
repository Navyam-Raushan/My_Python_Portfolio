import smtplib
import ssl

# This is for the connection.
host = "smtp.gmail.com"
port = 465

# This password is created by google and only used by this app.
username = "bsarthak935@gmail.com"
password = "lupwevndnduujnys"

receiver = "navyamraushan@gmail.com"
# Context means to send mail securely *using ssl.
context = ssl.create_default_context()

# First line will act like subject (don't forget \)
message = """\
Subject: First automated Mail
Hi
Its first automated mail from python.
check it out.
"""

# order does matter while providing parameters down see implementation.
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    #     to send emails
    server.sendmail(username, receiver, message)
