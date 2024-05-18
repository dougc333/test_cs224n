import socketserver

class Proxy(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print(f"Received {self.data} from {self.client_address[0]}")

        # Send the data to the server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(("server.com", 80))
        server.sendall(self.data)

        # Receive the data from the server and send it back to the client
        data = server.recv(1024)
        self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    with socketserver.TCPServer((HOST, PORT), Proxy) as server:
        server.serve_forever()
