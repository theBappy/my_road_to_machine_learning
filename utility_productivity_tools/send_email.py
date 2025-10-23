
import smtplib
import os


user_email = os.environ["EMAIL_USER"]
user_password = os.environ["EMAIL_PASS"]
receiver_email = input("Enter the receiver email address: ")

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.ehlo()

smtp_server.starttls()
smtp_server.ehlo()

smtp_server.login(user_email, user_password)

msg_to_be_sent = """
    Hello, receiver!
    Hope you are doing well.
    """

smtp_server.sendmail(
    user_email,
    receiver_email,
    msg_to_be_sent
)
print("Successfully sent the mail!")

smtp_server.quit()



