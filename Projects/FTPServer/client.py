import socket
import pickle
import tkinter as tk
import tkinter.filedialog as filedialog

class Client: 
    def __init__(self):
        self.HEADER = 64
        self.DISCONNECT = 'QUIT'
        self.FORMAT = 'utf-8'

        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = self.SERVER, self.PORT
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self, file_path):
        with open(file_path, 'rb') as file:
            data: bytes = file.read()
        self.client.send(data)

def open_file() -> str:
    my_folder: str = '/Users/yuvalsavaryegolandesman/Desktop/networking/FTP_server/my files'
    file_path: str = filedialog.askopenfilename(initialdir=my_folder)
    return file_path

def upload_file(client_socket: Client) -> bool:
    client_socket.send(open_file())
    print('uploading files...')
    return True

def get_file(client_socket: Client) -> bool:
    print('command not supported: [get]')
    return True

def quit_program(client_socket: Client) -> bool:
    print('command not supported: [get]')
    return False

if __name__ == "__main__" :

    functions: dict = {
        'q': lambda: upload_file(client_socket),
        'get': lambda: upload_file(client_socket),
        'upload': lambda: upload_file(client_socket),
    }

    connection = True
    client_socket = Client()
    while connection:
        command = input("Options: [q] Quit | [get] Retrieve Files | [upload] Upload Files\nEnter a command: ")
        if command in functions:
            connection = functions[command]()
        else:
            print(f'command not found: {command}')