import os
import platform as plat
import psutil
# get the basic information of the software
report = open("report.txt", "w")

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
# CPU frequencies
cpufreq = psutil.cpu_freq()
report.write(f"maxfreq: {cpufreq.max:.2f}Mhz \n")
report.write(f"minfreq: {cpufreq.min:.2f}Mhz \n")
ram_in_o = str(psutil.virtual_memory()[0])

ram_in_MB = ram_in_o[0:2]
report.write("ramtot: {}GB".format(ram_in_MB))

