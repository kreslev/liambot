import smtplib, ssl
from datetime import datetime
import os

#This file sets up, constructs, and sends email.

def sendEmail(sender, post):
    
    #Sets up email connection.
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "liambotdiscord@gmail.com"  # Enter your address
    receiver_emails = ["jordanholt@leeuniversity.edu", "david.wesley.jackson@gmail.com"]  # Enter receiver address
    password = os.getenv('EMAIL_TOKEN')
    
    #Gets current time
    dt = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    
    #Constructs email
    message = "Subject: " + sender + " requests help.\n\n"
    message += "At " + dt + " help was requested by " + sender + ". "
    message += "Along with the following message:\n"
    message += post

    #Sends email to addresses in array
    context = ssl.create_default_context()
    for emails in receiver_emails:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, emails, message)