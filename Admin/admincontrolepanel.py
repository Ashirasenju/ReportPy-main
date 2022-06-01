import socket
import sqlite3

print("[INFO] Initializing database")
try:
    con = sqlite3.connect('users')
    cur = con.cursor()
    print("[INFO] Database succesfully loaded")
except:
    print("[ALERT] Failed initializing database")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('127.0.0.1', 5566))
socket.listen(5)
client, address = socket.accept()
print("{} connected".format(address))
id = client.recv(1024).decode()
print(id)

cur.execute(id)
con.commit()
con.close()