from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import time
import os
import cam_server


# host = '10.200.0.2'
# host = '192.168.178.49'
host = '0.0.0.0'
port = 8000

class MyHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

            current_path = os.path.realpath(os.path.dirname(__file__))

            if self.path == '/':
                self.send_response(301)
                self.send_header('Location', '/index.html')
                self.end_headers()
            elif self.path == '/index.html':
                content = ''
                with open (os.path.join(current_path, 'templates', 'index.html'), 'r') as f:
                    content = f.read()
                    content = content.encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(content))
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404)
                self.end_headers()

class ControlServer(socketserver.ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == "__main__":

    # Start camera server
    cam_server.main()

"""     try:
        address = (host, port)
        server = ControlServer(address, MyHttpRequestHandler)
        server.serve_forever()
    except Exception as e:
        print(e) """





