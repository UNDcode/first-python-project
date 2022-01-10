# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)
              

applicant_list=[]


from account import *
from imap_tools import MailBox

with MailBox("imap.gmail.com", 993).login(Email_address, Email_password, initial_folder="INBOX") as mailbox:
    index=1
    for msg in mailbox.fetch('(SENTSINCE 01-Apr-2021)'): #2021년 4월 1일 이후로 온 메일 조회
        if "파이썬 특강 신청합니다." in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번 : {} /닉네임 : {} /전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index +=1

for applicant in applicant_list:
    print(applicant)