from email.message import EmailMessage
import smtplib
import imghdr
from lib2to3.pgen2.token import RBRACE

SMTP_SERVER = "smtp.gmail .com"
SMTP_PORT = 465

def sendEmail(addr):
    import re
    if bool(re.match('(^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9-]+.[a-zA-Z]{2,3}$)', addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")

message["Subject"] = "이것은 제목입니다."
message["From"] = "wonesther123@gmail.com"
message["To"] = "wonesther123@gmail.com"

with open("스크린샷(1).png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('스크린샷(1)', image_file)
message.add_attachment(image_file, maintype = 'image', subtype = image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("wonesther123@gmail.com","")

sendEmail("wonesther123@gmail.com")

smtp.quit()