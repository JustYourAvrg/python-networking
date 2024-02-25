import socket


# Create the server class
class Server:
    # Initialize the server class
    def __init__(self):
        # Set the host and port
        self.host = 'localhost'
        self.port = 8080
    

    # Handle the server
    def handle(self, host, port):
        # Try to handle the server
        try:
            # Create a socket object
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen()

            # Accept the connection
            conn, addr = server.accept()
            with conn:
                print(f"{addr} has connected.")

                # Receive and send data
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

            # Close the connection
            server.close()
            print("Server has closed.")
        
        # Handle any exceptions
        except Exception as e:
            print(f"An error occurred: {e}")
            server.close()


# Run the server
if __name__ == "__main__":
    server = Server()
    server.handle(server.host, server.port)
