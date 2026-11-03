import socket
s=socket.socket()
host = socket.gethostname()
port = 2797
s.connect((host,port))
print(s.recv(1024),decode())
s.close()