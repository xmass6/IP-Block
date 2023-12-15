import socket
import os

def check_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 0))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(0.2)
    try:
        message, address = s.recvfrom(8192)
        return address[0]
    except socket.timeout:
        return None

blocked_ips = {"<IP address>"}

def block_ip(ip_address):
    os.system("netsh advfirewall firewall add rule name='BlockIP' dir=in interface=any action=block remoteip=" + ip_address)
    blocked_ips[ip_address] = True

while True:
    ip_address = check_ip()
    if ip_address in blocked_ips:
        print(f"Blocking IP: {ip_address}")
        block_ip(ip_address)