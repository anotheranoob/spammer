# Copyright (c) 2018 Joshua Wang with MIT Licensing.
# See LICENSE on github page for more details.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

def check(x):
    try:
        if "." not in x.split("@")[1] and "@" not in x:
            return True

    except:
        return True

j=open("private/secret.json",'r').read()

pj = json.loads(j)
own = pj["email"]
pwd = pj["password"]
going = str(input("Which email to spam? ").strip())
amount = int(input("How much to spam? ").strip())
if check(going):
    print("Uh oh, that didn't appear to be a valid email. Please try again")

else:
    mail = MIMEMultipart()
    mail['From'] = own
    mail['To'] = going
    mail['Subject'] = "SPAM"
    body = "SPAM"
    mail.attach(MIMEText(body, 'plain'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(own, pwd)
    text = mail.as_string()
    for i in range(amount):
        s.sendmail(own, going, text)
        
    s.quit()

    print("The deed's been done. Have a good day.")
