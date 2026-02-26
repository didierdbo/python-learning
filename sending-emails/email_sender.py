import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # os.path
# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/

app_password = "cxys xkax pirs upmz"


html = Template(Path('sending-emails/index.html').read_text())

email = EmailMessage()
email['from'] = 'Didier Bonnet'
email['to'] = 'didier.dbo@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(name='TinTin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('didier.dbo@gmail.com', app_password)
    smtp.send_message(email)
    print('all good boss!')