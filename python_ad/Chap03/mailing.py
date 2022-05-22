# email.message기능만 import
from email.message import EmailMessage
import smtplib
import imghdr   # image 확장자
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465     # google SMTP server 포트 주소

# 유효성 검사 함수
def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("성공적으로 메일을 보냈습니다.")
    else:
        print("유효하지 않은 이메일 주소입니다.")

message = EmailMessage()

message.set_content("[본문] 배고프다 저녁 뭐먹지")
message["Subject"] = "[제목] 코드라이언 수강중"
message["From"] = "parkmihyunn@gmail.com"
message["To"] = "parkmihyunn@gmail.com"

# close() 필요X
with open("hhh.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('hhh',image_file)
message.add_attachment(image_file, maintype='image',subtype=image_type)

# 메일 서버 연결 후, 로그인
smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("parkmihyunn@gmail.com","algus830385^^")
sendEmail("parkmihyunn@gmail.com")
smtp.quit()