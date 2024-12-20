#! /usr/bin/python3

import socket
import os
import struct
import subprocess
from fcntl import ioctl

TUNSETIFF =0x400454ca
IFF_TUN = 0x0001
IFF_NO_PI = 0x1000

def open_tun(devname):
    fd = os.open('/dev/net/tun', os.O_RDWR)
    ifr = struct.pack("16sH", devname, IFF_TUN | IFF_NO_PI)
    ifs = ioctl(fd, TUNSETIFF, ifr)
    return fd


def ip_add(devname, ip_address):
    subprocess.run(['ip', 'addr', 'add', ip_address, 'dev', devname], check=True)
    subprocess.run(['ip', 'link', 'set', 'dev', devname, 'up'], check=True)
fd = open_tun(b'asa0')

ip_add('asa0', '10.10.2.1/24')

while True:
    buffer = os.read(fd, 1600)
    print(buffer)
