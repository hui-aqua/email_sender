import time
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_sender = 'hui.reboot@gmail.com'  # Your email
password_sender = 'Ch19911011'  # Your email account password
email_receiver = 'chenghui.qd@live.cn'  # Who you are sending the message to

# Message content
host_name = os.uname()[1]
subject = 'Message from ' + str(host_name)  # The subject line

msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subject


def send_alarm(filename):
    filename = "dfe"
    message = str(filename) + str("\n\n is dead!\n Please login and check!\n")
    # read the last 50 line
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines[-50:]:
        message += line + str("\n")
    message += "\nAbove is the last 50 lines\n"

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
    server.starttls()  # Use TLS
    server.login(email_sender, password_sender)  # Login to the email server
    text = msg.as_string()  # You now need to convert the MIMEMultipart object to a string to send
    server.sendmail(email_sender, email_receiver, text)
    server.quit()


def main(filename):
    while 1 < 3:
        b1 = os.path.getsize(filename)
        time.sleep(60)
        b2 = os.path.getsize(filename)
        if b1 == b2:
            send_alarm(filename)
            exit()
        else:
            time.sleep(10)


# main body
file = sys.argv[1]
if os.path.isfile(file):
    print("Now the file\n" + str(file) +
          "\nis monitoring")
    main(file)
else:
    print("Please ensure that the file is existed" + str(file))
    exit()
