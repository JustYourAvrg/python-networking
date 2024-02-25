import socket


# Create the client class
class Client:
    # Initialize the client class
    def __init__(self):
        # Set the host and port
        self.host = 'localhost'
        self.port = 8080

    
    # Connect to the server
    def connect(self, host, port):
        # Try to connect to the server
        try:
            # Create a socket object
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))

            # Send and receive data
            send_data = input("Enter a message: ")
            client.sendall(send_data.encode())

            recv_data = client.recv(1024)
            print(f"Received: {recv_data.decode()}")

            # Close the connection
            client.close()

        # Handle any exceptions
        except Exception as e:
            print(f"An error occurred: {e}")
            client.close()


# Run the client
if __name__ == "__main__":
    client = Client()
    client.connect(client.host, client.port)
