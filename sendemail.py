from email.message import EmailMessage
import imghdr
import smtplib, os

USER_EMAIL = "rajaachandramohan@gmail.com"
PASS = os.getenv("aivideo")
def send_email(imgpth):
    print("email_thread has started")
    email_message= EmailMessage()
    email_message['subject']= "A new prospect has arrived!"
    email_message.set_content("Welcome, your new customer!")
    with open(imgpth,'rb') as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    serv = smtplib.SMTP("smtp.gmail.com", 587)
    serv.ehlo()
    serv.starttls()
    serv.login(USER_EMAIL, PASS)
    serv.sendmail(USER_EMAIL, "rajaachandramohan@gmail.com", email_message.as_string())
    print("email sent")
    print("email_thread has completed")

    serv.quit()
