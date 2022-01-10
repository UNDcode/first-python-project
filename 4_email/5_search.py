from imap_tools import MailBox  #(pip install imap_tools)
from account import*

#mailbox= MailBox("imap.gmail.com", 993)
#mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    #for msg in mailbox.fetch():  #전체 메일 다 가져오기
        #print("[{}] {}".format(msg.from_, msg.subject))  


    #for msg in mailbox.fetch('(UNSEEN)'):  #읽지 않은 메일 가져오기
        #print("[{}] {}".format(msg.from_, msg.subject))  


    #for msg in mailbox.fetch('(FROM jdh3118@bu.ac.kr)', limit=2, reverse=True):  #특정인이 보낸 메일 가져오기
        #print("[{}] {}".format(msg.from_, msg.subject))  


    #for msg in mailbox.fetch(limit=2,reverse=True):  #최근 2개메일만 가져오기
          #print("[{}] {}".format(msg.from_, msg.subject)) 


     #for msg in mailbox.fetch('(TEXT "cloud")'): # cloud 글자를 포함하는 메일 가져오기(제목,본문) {한글불가} 
         #print("[{}] {}".format(msg.from_, msg.subject)) 
         

     #for msg in mailbox.fetch('(SUBJECT "ZOOM")'): # ZOOM 글자를 포함하는 메일 가져오기(제목만) {한글불가}    
         #print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailbox.fetch(limit=14,reverse=True):   # 제목에 '시발련아' 글자를 포함하는 메일 가져오기 {한글가능}
        if "시발련아" in msg.subject:
            print("[{}] {}".format(msg.from_, msg.subject)) 

     #for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)',limit=7,reverse=True): #특정 날짜 이후의 메일 가져오기(7개,최근순으로)
         #print("[{}] {}".format(msg.from_, msg.subject))

   
     #for msg in mailbox.fetch('(ON 07-Nov-2020)'): # 특정 날짜에 온 메일 가져오기 
         #print("[{}] {}".format(msg.from_, msg.subject))


    
    #2가지 이상의 조건을 모두 만족하는 메일(그리고 조건)
     #for msg in mailbox.fetch('(ON 07-Nov-2020 SUBJECT "ZOOM")'):
         #print("[{}] {}".format(msg.from_, msg.subject))

    #2가지 이상의 조건중 하나라도 만족하는 메일(또는 조건)
    #for msg in mailbox.fetch('(OR ON 07-Nov-2020 SUBJECT "Gmail")'):
       # print("[{}] {}".format(msg.from_, msg.subject))



     

              

