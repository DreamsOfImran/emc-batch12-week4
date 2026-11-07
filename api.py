import json
from http.server import BaseHTTPRequestHandler, HTTPServer

todos = [{"id": 1, "task": "Learning API"}]


class Handler(BaseHTTPRequestHandler):
    def send_json(self, code, data):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path == "/todos":
            self.send_json(200, todos)
        else:
            self.send_json(404, {"error": "Not Found!!"})

    def do_POST(self):
        if self.path == "/todos":
            length = int(self.headers.get("Content-Length", 0))
            item = json.loads(self.rfile.read(length))
            item["id"] = len(todos) + 1
            todos.append(item)
            self.send_json(201, item)


HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
