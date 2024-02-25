import socket


class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8080
    

    def handle(self, host, port):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen()

            conn, addr = server.accept()
            with conn:
                print(f"{addr} has connected.")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

            server.close()
            print("Server has closed.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            server.close()


if __name__ == "__main__":
    server = Server()
    server.handle(server.host, server.port)
