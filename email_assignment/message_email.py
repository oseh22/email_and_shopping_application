import smtplib
from email.message import EmailMessage

sender = "ose391@gmail.com"
password = ""
recipients_str = input("Enter recipient email address: ")
recipients = recipients_str.split(",")
Subject = input("Subject of the mail: ")
name = input("input your name: ")
body = input("Enter email body: ")

msg = EmailMessage()
msg.set_content(body)

msg['From'] = f"{ sender} , {name} "
msg['To'] =recipients_str
msg['Subject'] =Subject


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)
print ('message sent successful')