import http.server
import socketserver
from jinja2 import Template;

PORT = 8001

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/todo':
            template = Template(open('todo.html').read())
            title = "This is todo list 1"
            name = "Mehrzad"
            todo_list = [
                {"name":"Mehrzad", "age":"24"},
                {"name":"Mohammad", "age":"25"},
                ]
            content = template.render(title=title, name=name, todo_list=todo_list)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes(content,'utf-8'))
            return 
            
        if self.path == '/api':
            with open('data.json', 'r') as f:
                html = f.read()

            # Send a response with the HTML content
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(html, 'utf-8'))
            return 
        if self.path == '/about':
            with open('about.html', 'r') as f:
                html = f.read()

            # Send a response with the HTML content
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(html, 'utf-8'))
            return
        if self.path == '/':
            with open('index.html', 'r') as f:
                html = f.read()

            # Send a response with the HTML content
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(html, 'utf-8'))
            return
        else:
            self.send_error(404)
            return


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
