import asyncio


class Server(asyncio.Protocol):
    def __init__(self, conns, loop):
        # Store connections and event loop
        self.conns = conns
        self.loop = loop


    # When a client connects, add the connection to the list
    def connection_made(self, transport):
        self.conns += [transport]
        self.transport = transport
        print(f'Connection made: {transport.get_extra_info("peername")}')
    

    # When a client disconnects, remove the connection from the list
    def connection_lost(self, exc):
        self.conns.remove(self.transport)
        print(f'Connection lost: {self.transport.get_extra_info("peername")}')
    

    # When data is received, send it to all connections
    def data_received(self, data):
        if data:
            print(data.decode())
            for connection in self.conns:
                connection.write(data)
                print(f'Sent to {connection.get_extra_info("peername")} | {data.decode()}')
            

if __name__ == '__main__':
    # List to store connections
    conns = []

    # Create event loop and server
    loop = asyncio.get_event_loop()
    conn = loop.create_server(lambda: Server(conns, loop), 'localhost', 8888)
    
    # Start server
    server = loop.run_until_complete(conn)

    # Run server until KeyboardInterrupt
    try:
        loop.run_forever()
    
    except KeyboardInterrupt:
        pass
    
    # Close server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
