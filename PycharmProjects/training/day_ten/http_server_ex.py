#Create a HTTP server

from BasicHttpServer import HTTPServer,CGIHTTPRequestHandler
#BaseHTTPRequestHandler

# import BasicHttpServer
# dir(BasicHttpServer)
# ['BasicHttpServer', 'CGIHTTPRequestHandler', 'HTTPServer', 'OptionParser', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'main']

class HelloHandler(CGIHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200, 'OK')
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"""<HTML>
            <HEAD><TITLE>Hello</TITLE></HEAD>
            <BODY>Hello World!</BODY></HTML>""")

serv = HTTPServer(("", 8080), HelloHandler)
serv.serve_forever()

#server runs if u run the code
#Then go to browser

#http://localhost:8080/hello
# <HTML>
#             <HEAD><TITLE>Hello</TITLE></HEAD>
#             <BODY>Hello World!</BODY></HTML>


#127.0.0.1 - - [30/Oct/2018 12:26:11] "GET /hello HTTP/1.1" 200 -





