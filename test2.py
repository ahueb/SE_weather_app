import http.server
import socketserver

class request_handler(http.server.SimpleHTTPRequestHandler):
    def get_req(self):
        if self.path == '/':
            self.path = './web/index.html'
        return http.server.SimpleHTTPRequestHandler(self)

handler = request_handler

port = 8080
server = socketserver.TCPServer(("", port), handler)

server.serve_forever()