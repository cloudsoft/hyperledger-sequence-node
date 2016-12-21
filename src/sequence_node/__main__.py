#!/usr/bin/env python

from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler

SEQUENCE = 0

class SequenceNodeHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global SEQUENCE

        self.send_response(200)
        self.send_header("Content-type:", "text/plain")

        self.wfile.write("\n")
        self.wfile.write(SEQUENCE)

        SEQUENCE += 1

def main():
    server = HTTPServer(("0.0.0.0", 9999), SequenceNodeHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
