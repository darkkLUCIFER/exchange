import smtplib

from config import rules
from local_config import MAILGUN_APIKEY
# make local_config.py in your project and add your MAILGUN_APIKEY to that

from email.mime.text import MIMEText


# customize this part with your email settings(also you can use mailtrap.io site for making test)
def send_smtp_email(subject, body):
    msg = MIMEText('Testing some Mailgun awesomness')
    msg['Subject'] = "Hello"
    msg['From'] = "foo@YOUR_DOMAIN_NAME"
    msg['To'] = rules['email']['receiver']

    with smtplib.SMTP('smtp.mailgun.org', 587) as mail_server:
        mail_server.login('postmaster@YOUR_DOMAIN_NAME', MAILGUN_APIKEY)
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
        mail_server.quit()
