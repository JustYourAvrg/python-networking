import socket
import threading
import sys

from utils import help_prompt, check_nickname_input


class Client:    
    def handle_input(self):
        while True:
            message = input("")
            self.send_message(message)
    

    def handle_receive(self):
        while True:
            try:
                message = self.client.recv(1024)
                
                if message == b"SERVER_COMMANDS_HELP":
                    self.server_commands_help()

                else:
                    print(message.decode())

            except socket.error:
                break
    

    def server_commands_help(self):
        print(help_prompt)


    def send_message(self, message):
        self.client.send(message.encode())


    def start(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        server_data = self.client.recv(1024).decode()
        if server_data == "CLIENT_NICKNAME_REQUEST":
            nickname = input("Enter a nickname >>> ")
            nick_check = check_nickname_input(nickname)
            if nick_check is True:
                self.client.send(nickname.encode())
            else:
                print(f"Nickname ERROR | {nick_check}")
                self.client.close()
                sys.exit()
        
        self.handle_receive_thread = threading.Thread(target=self.handle_receive)
        self.handle_receive_thread.start()

        self.handle_input_thread = threading.Thread(target=self.handle_input)
        self.handle_input_thread.start()


if __name__ == "__main__":
    client = Client()
    client.start(host='localhost', port=8080)
