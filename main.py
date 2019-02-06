#!C:\Program Files (x86)\Python37-32\python.exe
#coding=utf-8
# client
import time
import datetime
import socket
import reporting
import threading

def main():
    while(1):
        print(str(datetime.datetime.now()))
        login_thread = threading.Thread(target = conn,args = ('118.233.34.140', 6901,'登入伺服器'))
        char_thread = threading.Thread(target = conn, args = ('118.233.34.140', 6122,'角色伺服器'))
        map_thread = threading.Thread(target = conn, args = ('118.233.34.140', 5122,'地圖伺服器'))
        login_thread.start()
        char_thread.start()
        map_thread.start()
        login_thread.join()
        char_thread.join()
        map_thread.join()
        time.sleep(5)
    
    if(1):
      """  try:
            address = ('118.233.34.140', 6901)
        except:
            print("登入伺服器異常")
            reporting.reporting()
            time.sleep(60)
            time.sleep(3.1)

"""

def conn(ip, port, typ):
    try:
        address = (ip, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        s.close()
        print(typ+' 正常\n')
    except:
        print(typ+' 異常\n')
        reporting.reporting(typ)
        time.sleep(3600)
if __name__ == "__main__":
    print("Content-type: text/html")
    print("")
    main()
