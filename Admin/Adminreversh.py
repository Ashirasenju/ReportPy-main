import socket
import pickle

HOST = "127.0.0.1"
PORT = 5566


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:

        cmd = input(">")
        if cmd == ("exit"):
            break

        s.sendall(str.encode(cmd))
        data = s.recv(1024)
        print(data.decode())
        pass


