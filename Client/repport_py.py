import subprocess
import platform as plat
import psutil
import uuid
import os
import socket

# get the basic information of the software
report = open("report.txt", "a+")

id = open("id.txt", "a+")
if os.stat("id.txt").st_size == 0:
    id.write(str(uuid.uuid4()))

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

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    id_file = open("id.txt")
    id = id_file.read()
    s.send(id.encode())
    req = cur = f"INSERT INTO users (ID, MACHINE_NAME, IP, MAC_ADDR, PLAFORM, SYS, VER_SYS, BITS_SYS, TOTCORE, MAXFREQ, MINFREQ, RAMTOT, BROADCAST_IP, NETMASK, BROADCAST_MAC) values ('{id}', '{computer_name}', '{ip_addr}', '{mac_addr}', '{platform}', '{system}', '{ver}', '{bits}', '{totcore}', '{maxfreq}', '{minfreq}', {ram_in_MB}, '{broadcast_ip}', '{netmask}', '{BROADCAST_MAC}');".encode()
    print(req)
    s.send(req)

