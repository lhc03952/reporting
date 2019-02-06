#!C:\Program Files (x86)\Python37-32\python.exe
#coding=utf-8
# client
import time
import datetime
import socket
import threading

def main():
     print(str(datetime.datetime.now())+'<br>')
     login_thread = threading.Thread(target = conn,args = ('118.233.34.140', 6901,'登入伺服器'))
     char_thread = threading.Thread(target = conn, args = ('118.233.34.140', 6122,'角色伺服器'))
     map_thread = threading.Thread(target = conn, args = ('118.233.34.140', 5122,'地圖伺服器'))
     login_thread.start()
     char_thread.start()
     map_thread.start()
     login_thread.join()
     char_thread.join()
     map_thread.join()
    
def conn(ip, port, typ):
    try:
        address = (ip, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        s.close()
        print(typ+' 正常<br>')
    except:
        print(typ+' 異常<br>')
if __name__ == "__main__":
    print("Content-type: text/html")
    print("")
    main()
