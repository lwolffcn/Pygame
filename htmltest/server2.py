from socketserver import TCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        str1 = 'Got connection from'
        str1 = str1.encode()
        str2 = 'Thank you for connecting'
        str2 = str2.encode()
        print(str1, addr)
        self.wfile.write(str2)

server = TCPServer(('lf', 1234), Handler)
server.serve_forever()