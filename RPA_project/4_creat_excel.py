import smtplib  # 이메일 전송
from openpyxl import Workbook # 엑셀 불러오기 (pip install openpyxl)
from account import * # 계정 불러오기 
from random import*   
from imap_tools import MailBox # 이메일 조회 
from email.message import EmailMessage # 이메일 전송 




print("[50명 지원자 이메일 전송]")
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

    





applicant_list = [] # 지원자 리스트 
max_val = 40 #최대 선정자 수 
print("[1. 지원자 메일 조회]")
with MailBox("imap.gmail.com", 993).login(Email_address, Email_password, initial_folder="INBOX") as mailbox:
    index=1
    for msg in mailbox.fetch('(SENTSINCE 01-Apr-2021)'): #2021년 4월 1일 이후로 온 메일 조회
        if "파이썬 특강 신청합니다." in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            #print("순번 : {} /닉네임 : {} /전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))   
            index +=1                                                #반복문을 통해 수정된 리스트: applicant_list= [(msg,index,nickname,phone),(msg,index,mickname,phone),(msg,index,nickname,phone)......]


print("[2. 선정 / 탈락 메일 발송]")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(Email_address, Email_password)

    for applicant in applicant_list:

        to_addr = applicant[0].from_ #수신 메일 주소
        #index = applicant[1]
         #nickname = applicant[2]
         #phone = applicant[3] 
        index, nickname, phone = applicant[1:]

        title = None
        content = None
         
        if index <= max_val:
             title = "파이썬 특강 안내 [선정]"
             content = "{}님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 {}번)".format(nickname, index)
    
        else:
            title = "파이썬 특강 안내 [탈락]"
            content = "{}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {})".format(nickname, index-max_val)
        
        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = Email_address
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname, "님에게 메일 발송 완료") 


print("[3. 선정자 명단 파일 생성]")
wb = Workbook()
ws = wb.active
ws.append(["순번","닉네임", "전화번호"]) # a1셀에 순번, b1셀에 닉네임, c1셀에 전화번호가 들어감

for applicant in applicant_list[:max_val]:
    ws.append(applicant[1:])
    # index = applicant[1]
    # nickname = applicant[2]
    # phone = applicant[3]
    # ws.append([index, nickname, phone])

wb.save("email_2.xlsx")

print("모든 작업이 완료되었습니다.")
     
 
                  
 





#[선정 명단 엑셀]
#순번 닉네임 전화번호
#1   유재석  9429
#2   박명수  2463
#3   정형돈  9236