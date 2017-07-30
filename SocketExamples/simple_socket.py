#need to specify the kind of stream TCP or UDP
#SOCK_DGRAM  for UDP/IP
#SOCK_STREAM  for TCP/IP
#AF_INET is for IPv4
#AP_INET6 is for IPv6

import socket

def print_hostname_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("host name: {}".format(host_name))
    print("IP address: {}".format(ip_address))
    
print_hostname_info()
