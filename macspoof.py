#Importing relevant modules
import random
import os
import subprocess

#function to return a random character for the MAC address
def get_random():
    return random.choice("abcdef0123456789")

# Fuction to create a new mac address
def new_mac():
    new = ""
    for i in range(0,5):
        new += get_random()+get_random+":"
    new += get_random()+get_random()
    return new

#Changing MAC with system calls

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

#Turning eth0 down
subprocess.call(["sudo", "ifconfig","eth0","dowm"])

#Instantiating new MAC address
new_m = new_mac()

#Assigning new MAC address
subprocess.call(["sudo", "ifconfig", "eth0", "hw","ether","%s"%new_m])

#Turning eth0 on with new mac address
subprocess.call(["sudo", "ifconfig","eth0","up"])

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))