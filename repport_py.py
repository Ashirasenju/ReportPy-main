import os
import platform as plat

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


report.write("HARDWARE \n")

