import socket
import pickle


def reverse_sh(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:

            cmd = input(">")
            if cmd == ("exit"):
                break

            s.sendall(str.encode(cmd))
            data = s.recv(1024)
            return data.decode()
            pass
