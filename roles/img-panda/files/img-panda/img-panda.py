#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os, random

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        rndpanda = random.choice(os.listdir("./resources/"))
        f = open("./resources/" + rndpanda, 'rb')
        self.send_response(200)
        self.send_header('Content-type', 'image/jpg')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()
        return

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()


if __name__ == "__main__":
    run()
