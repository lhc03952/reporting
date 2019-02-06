#!C:\Program Files (x86)\Python37-32\python.exe
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime

def reporting(ser_typ):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('hahahauccu11@gmail.com','z147896325')#第一個參數是電郵帳號，第二個參數是密碼
    to = ["77520tou@gmail.com", "lhc03952@gmail.com", "jamexup6@gmail.com"]  #收件者的電郵地址，為list資料型態
    #　電子郵件內文
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('系統偵測到 '+ser_typ+' server 異常！\n'+(str(datetime.datetime.now())), 'plain', 'utf-8')
    # 发送者
    message['From'] = Header("Reina Ragnarok", 'utf-8')
    # 接收者
    message['To'] =  Header("Reina 維護團隊", 'utf-8') 
    subject = 'Reina Ragnarok伺服器偵測到異常！'
    message['Subject'] = Header(subject, 'utf-8')
    #利用sendmail 這個method 來寄出電郵，SMTP.sendmail(from_addr, to_addrs, msg, mail_options=[], rcpt_options=[])
    smtpObj.sendmail("hahahauccu11@gmail.com", to, message.as_string())
    #關閉本地端對遠端郵件伺服器的連線
    smtpObj.quit()
