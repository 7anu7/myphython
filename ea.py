import smtplib
import getpass

myemail=input("your email id : ")
password=getpass.getpass()
recemail = input("Receiver's email id : ")
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(myemail,password)
message = "Message_you_need_to_send"
s.sendmail(myemail,recemail,message)
s.quit()