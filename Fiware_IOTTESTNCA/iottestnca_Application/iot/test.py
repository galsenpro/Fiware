import socket
ip = socket.gethostbyname(socket.gethostname())
#d = socket._LOCALHOST()
d = socket.gethostbyaddr(ip)
print(ip)
print(d)