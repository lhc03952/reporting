#!C:\Program Files (x86)\Python37-32\python.exe
#coding=utf-8
# client
import time
import socket
import reporting
import _thread
def main():
    while(1):
        try:
            address = ('118.233.34.140', 6901)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(address)
            print("登入伺服器正常")
            time.sleep(3.1)
        except:
            print("登入伺服器異常")
            reporting.reporting()
            time.sleep(60)

if __name__ == "__main__":
    print("Content-type: text/html")
    print("")
    main()
