# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:52:22 2020

@author: HP PC
"""

from smtplib import SMTP

# Set up a connection to SMTP server. If you use a SSL server use the 465 port with the SMTP_SSL function
smtpObj = SMTP('smtp.gmail.com', 587)

# Sending the SMTP 'Hello' message. This greeting is the first step in SMTP and is important for establishing a connection to the server. If the first item in the returned tuple is the integer 250 (the code for “success” in SMTP), then the greeting succeeded.
smtpObj.ehlo()

# Starting TLS encryption. If you are connecting to port 465 (using SSL), then encryption is already set up, and you should skip this step. starttls() puts your SMTP connection in TLS mode. The 220 in the return value tells you that the server is ready.
smtpObj.starttls()

# Logging in to the SMTP server. 235 in the return value means the login was accepted
email = input("Enter your email: ")
password = input("Enter password: ")
smtpObj.login(f'{email}', '{password}')

# Sending an email. The start of the email body string must begin with 'Subject: \n' for the subject line of the email. The '\n' newline character separates the subject line from the main body of the email.
smtpObj.sendmail(f'{email}', '{recipient_email}', 'Subject: Reminder!!\n')

# Disconnecting from the SMTP server. 221 means the session is ending
smtpObj.quit()

