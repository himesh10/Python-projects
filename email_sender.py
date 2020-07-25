import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Himesh Parmar"
email["to"] = "himesh10@hotmail.co.uk"
email["subject"] = "you won a million dollars"

email.set_content(html.substitute({"name": 'TinTin'}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login("himeshparm10@gmail.com", "itachi108")
	smtp.send_message(email)
	print("all good boss")
