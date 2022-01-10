from imap_tools import MailBox
from account import*

mailbox= MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")


#limit:최대 메일 갯수
# reverse : True 일 경우 최근 메일부터, False 일 경우 과거 메일부터
for msg in mailbox.fetch(limit=2, reverse=True):
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    print("날짜", msg.date)
    print("본문", msg.text)
    print("="*100)

    for att in msg.attachments:
        print("첨부파일이름", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)

        with open("download_"+att.filename,"wb") as f:
            f.write(att.payload)
            print("첨부 파일 {} 다운로드 완료".format(att.filename))


        
