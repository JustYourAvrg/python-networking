import socket
import threading


class Server:
    def __init__(self):
        self.clients = {}


    def send_to_all(self, message):
        for client in self.clients:
            client.send(message)


    def handle_clients(self, client):
        while True:
            try:
                message = client.recv(1024)

                if message == b"/help":
                    client.send(b"SERVER_COMMANDS_HELP")

                else:
                    msg = f"{self.clients[client]}: {message.decode()}"
                    self.send_to_all(msg.encode())
            

            except socket.error:
                self.send_to_all(f"{self.clients[client]} has left the chat".encode())
                del self.clients[client]
                break
    

    def handle_receive(self):
        while True:
            try:
                client, addr = self.server.accept()
                print(f"Client {addr} connected")

                client.send(b"CLIENT_NICKNAME_REQUEST")
                nickname = client.recv(1024).decode()

                self.clients[client] = nickname
                self.send_to_all(f"{nickname} has joined the chat".encode())

                thread = threading.Thread(target=self.handle_clients, args=(client,))
                thread.start()
            
            except socket.error:
                break
                

    def start(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()

        self.handle_receive()
        

if __name__ == "__main__":
    server = Server()
    server.start('localhost', 8080)
