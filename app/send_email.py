import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import current_app

def send_email(data):
    username = data.get("username")
    email = data.get("email")
    message = data.get("message")
    from_email = current_app.config["FROM_EMAIL"]
    to_email = current_app.config["TO_EMAIL"]
    password = current_app.config["APP_PASSWORD"]

    body =  f"name: {username} \n" \
            f"email: {email} \n" \
            f"message: {message}"

    msg = MIMEMultipart()
    msg["from"] = from_email
    msg["to"] = to_email
    msg["subject"] = "از طرف سایت portfolio!"
    msg.attach(MIMEText(body,"plain","utf-8"))

    email_host = current_app.config["EMAIL_HOST"]
    email_port = current_app.config["EMAIL_PORT"]
    try:
        with smtplib.SMTP_SSL(email_host,port=email_port) as server:
            server.login(from_email,password)
            server.send_message(msg)
        return True
    except Exception as e:
        current_app.logger.exception("Email sending failed!")
        return False
   