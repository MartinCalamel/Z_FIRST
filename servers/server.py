import http.server
import socketserver

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


with socketserver.TCPServer(("", 8000), QuietHandler) as httpd:
   print("Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ")
   httpd.serve_forever()
