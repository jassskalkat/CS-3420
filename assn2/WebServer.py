from http.server import HTTPServer, BaseHTTPRequestHandler

BIND_HOST = 'localhost'
PORT = 8000


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "No file with such name"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


print(f'Listening on http://{BIND_HOST}:{PORT}\n')

http = HTTPServer((BIND_HOST, PORT), HTTPRequestHandler)
http.serve_forever()
