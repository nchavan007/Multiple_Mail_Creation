#!/usr/bin/python3.6

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def sendmail(Title="Emp Table modified", receiver_email="test.testmail99999@gmail.com", msg="Test Message", Tmsg=" "):
    """ This function can be used for sending the mail with message which is provided as the argument """
    with open("Mail_Config", "r") as file:
        MailDetails=json.load(file)
    sender_email = MailDetails["sender_email"]
"""    receiver_email = MailDetails["receiver_email"]"""
    password = MailDetails["password"]


    message = MIMEMultipart("alternative")
    message["Subject"] = "{}".format(Title)
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """\
    <html>
      <body>
        <p>Hi There,<br><br>
           Greetings of the Day!!!!<br>
            <br>
            {}<br><br>
            {}<br>

        </p>
      </body>
    </html>
    """.format(msg,Tmsg)

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
