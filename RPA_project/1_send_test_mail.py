import smtplib
from random import*
from account import *
from email.message import EmailMessage 

nicknames=("재석","명수","형돈","홍철","세호","서연","서윤","지우","서현","민서","하은","하윤","윤서","지유","지민","채원","지윤","은서","수아","다은","예은","지아","수빈","소율","예린","예원","지원","소윤","지안","하린","시은","유진","채은","윤아","유나","가은","서영","민지","예진","서아","수민","수연","연우","예나","예서","주아","시연","연서","하율","다인")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:  # 리스트에있는 사람들을(nicknames) 한명씩 nickname에 저장하여 반복하는 구조 
        msg= EmailMessage()
        msg["Subject"]="파이썬 특강 신청합니다." # 제목
        msg["From"]=EMAIL_ADDRESS # 보내는 사람
        msg["To"]="jdh3118@bu.ac.kr" # 받는 사람
        
        content = nickname + "/" + str(randint(1000,9999))
        msg.set_content(content)
        smtp.send_message(msg)

        print(nickname+"님이 jdh3118@bu.ac.kr메일로 발송 완료.")         

    