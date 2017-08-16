import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()

def send_mail(fromAddr,toAddr,subject,text,password):
    msg['To']= toAddr
    msg ['From'] = fromAddr
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    try:

        #specify the smtp mail server and port (google server)
        mail= smtplib.SMTP('smtp.gmail.com', 587)

        #identufy urself to the server
        mail.ehlo() #esmtp, extened smtp

        #To encrytp the login and other methods
        mail.starttls()

        mail.login(fromAddr, password)

        mail.sendmail(fromAddr,toAddr,msg.as_string())

        #close the connection
        mail.close()

    except SMTPException:
        print ("Error: Unable to send email")
    
    
send_mail('*****@gmail.com','******@gmail.com','Test Python',"First Test with attachment",'**********')
