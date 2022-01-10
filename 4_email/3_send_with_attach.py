import smtplib
from account import *
from email.message import EmailMessage 

msg= EmailMessage()
msg["Subject"]="테스트 메일입니다" # 제목
msg["From"]=EMAIL_ADDRESS # 보내는 사람
msg["To"]="jdh3118@bu.ac.kr" # 받는 사람
msg.set_content("다운로드 하세요")


#구글에 MIME type 검색해서 첨부할 파일의 maintype과 subtype 알아낼수있음
with open("4주차 과제.pdf", "rb") as f:                  
    msg.add_attachment(f.read(),maintype="application",subtype="pdf",filename=f.name)

with open("엑셀파일.xlsx", "rb") as f:
    msg.add_attachment(f.read(),maintype="application",subtype="octet-stream",filename=f.name)
    

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)