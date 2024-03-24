import customtkinter as ctk
import asyncio

from tkinter import messagebox, simpledialog
from utils import nickname_checks


# CTK CONFIGURATION
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


class Client(asyncio.Protocol):
    def __init__(self, loop, nickname=None):
        # Store the event loop and nickname
        self.loop = loop
        self.nickname = nickname


    # When the connection is made, store the transport
    def connection_made(self, transport):
        self.transport = transport


    # When data is received, edit the text area
    def data_received(self, data):
        msg = data.decode()
        if msg:
            print(msg)
            self.edit_text(msg=msg)


    # Edit the text area
    def edit_text(self, msg):
        self.textArea.configure(state='normal')
        self.textArea.insert('end', f'{msg}\n')
        self.textArea.configure(state='disabled')
        self.textArea.see('end')

    
    # Send a message from the client to the server
    def send_msg(self):
        msg = self.msgInput.get()
        if msg:
            self.transport.write(f"{self.nickname}: {msg}".encode())
            self.msgInput.delete(0, 'end')


    # Run the GUI
    async def run_gui(self):
        try:
            while True:
                self.root.update()
                self.root.update_idletasks()
                await asyncio.sleep(0.01)
        
        # Close the GUI and loop if an exception occurs
        except Exception as e:
            print(e)
            self.root.destroy()
            self.loop.stop()
            self.loop.close()


    # Create the client GUI
    def client_gui(self):
        # Setup the root for the GUI
        self.root = ctk.CTk()
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.title('Chat Client')

        # Add GUI Components
        self.textArea = ctk.CTkTextbox(master=self.root, width=470, height=420, state='disabled')
        self.textArea.grid(row=0, column=0, padx=15, pady=10)

        self.msgInputFrame = ctk.CTkFrame(master=self.root)
        self.msgInputFrame.grid(row=1, column=0, pady=(5, 0))

        self.msgInputFrame.grid_columnconfigure((0, 1), weight=1)
        self.msgInputFrame.grid_rowconfigure(0, weight=0)

        # User input
        self.msgInput = ctk.CTkEntry(master=self.msgInputFrame, width=360, height=35)
        self.msgInput.grid(row=0, column=0, padx=(0, 10))

        # Run the send_msg function when the button is clicked
        self.msgBtn = ctk.CTkButton(master=self.msgInputFrame, width=80, height=35, text='Send', command=self.send_msg)
        self.msgBtn.grid(row=0, column=1, padx=(10, 0))

        # When the window is closed, stop the loop
        self.root.protocol('WM_DELETE_WINDOW', lambda: self.loop.stop())


if __name__ == '__main__':
    # Get the nickname
    nickname = simpledialog.askstring('Nickname', 'Enter a nickname')
    nickname_check = nickname_checks(nickname)
    if nickname_check != True:
        messagebox.showerror('Error', nickname_check)
        exit()

    # Create the event loop and client
    loop = asyncio.get_event_loop()
    client = Client(loop, nickname=nickname)
    
    # Connect to the server
    conn = loop.create_connection(lambda: client, 'localhost', 8888)
    server = loop.run_until_complete(conn)
    
    # Run the GUI
    try:
        client.client_gui()
        loop.create_task(client.run_gui())
        loop.run_forever()

    # Close the loop
    except Exception as e:
        loop.close()
        print(e)
    
    except KeyboardInterrupt:
        pass
