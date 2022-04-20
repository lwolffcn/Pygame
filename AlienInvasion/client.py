import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
#s.send('fdgdfgdgd')
str = 'this is client message test'
str = str.encode()
#s.send(str)
print(s.recv(1024))
print(s.recv(1024))
is_ture = True
while is_ture:
    #str = 'this is client message test'
    str = input('enter your word： ')
    if str == 'Q':
        str = str.encode()
        s.send(str)
        is_ture = False
    str = str.encode()
    s.send(str)