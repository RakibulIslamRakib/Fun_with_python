import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendmail(email,password,to_mail,subject,message):
    msg=MIMEMultipart()
    msg['From'] = email
    msg['To'] = to_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(message,'Plain'))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    text = msg.as_string()
    server.sendmail(email,to_mail,text)
    server.quit()

email = 'rakibulr312@gmail.com'
password = '01791742746'
to_mail = 'rakibulr310@gmail.com'
subject = 'this is subject'
message = 'this is message'

sendmail(email,password,to_mail,subject,message)
