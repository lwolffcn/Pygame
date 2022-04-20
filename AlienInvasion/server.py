import socket

s = socket.socket()
host = socket.gethostname()
#host = 'lf'
print(host)
port = 1234
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    #print(s.accept())
    print('Got connection from', c)
    print('Got connection from', addr)
    str = 'this is server message test'
    str = str.encode()
    str2 = 'this is server message test2'
    str3 = 'this is server message test2'
    #c.send(str3)
    c.send(bytes(str2, 'UTF-8'))
    c.send(str)
    #c.send('Thank you for connecting')
    print(c.recv(1024))
    c.close()