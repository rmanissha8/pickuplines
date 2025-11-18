import json
import random
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        with open("messages.json", "r") as f:
            data = json.load(f)

        message = random.choice(data["messages"])

        response = {"pickup_line": message}

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), SimpleAPI)
    print("Server running on http://localhost:8080")
    server.serve_forever()
