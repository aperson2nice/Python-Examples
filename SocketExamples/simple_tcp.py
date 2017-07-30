from socket import *

_host = "www.uis.edu"
_port = 80

client = socket(AF_INET, SOCK_STREAM)
client.connect((_host, _port))

client.send("GET / HTTP/1.1\r\nHost:www.uis.edu\r\n\r\n")

response = client.recv(10)
print(response)

client.close()