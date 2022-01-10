import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() #연결이 잘 수립되는지 확인
    smtp.starttls() #모든내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) #로그인

    subject = "test mail" #메일제목
    body = "mail body" #메일본문
    msg = f"Subject: {subject}\n{body}"

    smtp.sendmail(EMAIL_ADDRESS, "jdh3118@bu.ac.kr", msg) #메일보내기(발신자,수신자, 정해진 형식의 메시지 )



