import smtplib
import ssl


# creating function by refactor of pycharm
def send_mail(message):
    # This is for the connection.
    host = "smtp.gmail.com"
    port = 465
    # This password is created by google and only used by this app.
    username = "bsarthak935@gmail.com"
    password = "lupwevndnduujnys"

    # I am receiver in this case and this app will login me first.
    receiver = "bsarthak935@gmail.com"
    # Context means to send mail securely *using ssl.
    context = ssl.create_default_context()

    # order does matter while providing parameters down see implementation.
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        #     to send emails
        server.sendmail(username, receiver, message)
