import smtplib
from account import *
from email.message import EmailMessage 

msg= EmailMessage()
msg["Subject"]="테스트 메일입니다" # 제목
msg["From"]=EMAIL_ADDRESS # 보내는 사람
msg["To"]="jdh3118@bu.ac.kr" # 받는 사람


msg.set_content("테스트 본문입니다") #본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)