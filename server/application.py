"""Web server"""

import http.server
import socketserver

PORT = 8000

class TestMe():
    """Test class"""

    def take_five(self):
        """Take five unit test"""
        return 5

    def port(self):
        """Port unit test"""
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
