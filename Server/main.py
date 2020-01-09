from server import MyHandler
import socketserver

PORT = 80
handler = MyHandler
httpd = socketserver.TCPServer(('127.6.6.1', PORT), handler)
print("Server at PORT ", PORT)
httpd.serve_forever()
