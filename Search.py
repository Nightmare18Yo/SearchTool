from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/search'):
            query = self.path.split('=')[1]
            search_url = "https://www.google.com/search?q=" + query
            webbrowser.open(search_url, new=2)
            self.send_response(200)
            self.end_headers()
            return
        elif self.path == '/':
            self.send_response(200)
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
            return
        else:
            self.send_response(404)
            self.end_headers()
            return

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print("Server is running at http://localhost:8000/")
    httpd.serve_forever()



