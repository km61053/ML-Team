#smtplib defines SMTP client session that can be used to send emails using SMTP listener
import smtplib

#content= "Test email from python"

message = """From: From Sneha Bhattaram <***************@gmail.com>
To: To Sneha Bhattaram <********************@gmail.com>
Subject: SMTP e-mail test using Python

This is a test e-mail message.
"""
try:

    #specify the smtp mail server and port (google server)
    mail= smtplib.SMTP('smtp.gmail.com', 587)

    #identufy urself to the server
    mail.ehlo() #esmtp, extened smtp

    #To encrytp the login and other methods
    mail.starttls()

    mail.login('*******@gmail.com', '**********')

    mail.sendmail('********@gmail.com','*****@gmail.com',message)

    #close the connection
    mail.close()

except SMTPException:
    print ("Error: Unable to send email")
