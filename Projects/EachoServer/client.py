import socket

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

    def send(self, msg):
        if not isinstance(msg, bytes):
            messege = msg.encode(self.FORMAT)
        else:
            messege = msg

        msg_length = len(messege)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        self.client.send(send_length)
        self.client.send(messege)

        conf_length = self.client.recv(self.HEADER).decode(self.FORMAT)
        if conf_length:
            server_msg = self.client.recv(len(conf_length)).decode(self.FORMAT)
            print(f'[SERVER {self.ADDR}] {server_msg}')



if __name__ == "__main__" :
    connection = True
    client_socket = Client()
    while connection:
        msg = input('enter a messege: ')
        if msg.lower() == 'q':
            client_socket.send(client_socket.DISCONNECT)
            connection = False
        else:
            client_socket.send(msg)
