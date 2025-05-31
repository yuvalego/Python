import socket
import threading

class Server:
    def __init__(self) -> None:
        self.HEADER: int = 64
        self.DISCONNECT: str = 'QUIT'
        self.FORMAT: str = 'utf-8'

        self.PORT: int = 5050
        self.SERVER: str = socket.gethostbyname(socket.gethostname())
        self.ADDR: tuple = self.SERVER, self.PORT
        self.server: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

    def __handle_client(self, client_conn: socket, addr: tuple) -> None:
        print(f'[NEW CONNECTION] {addr} connected.')
        connection: bool = True
        while connection:
            msg_length = client_conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = client_conn.recv(msg_length).decode(self.FORMAT)

                send_conf: str = 'messege recived.'
                self.__send(client_conn, send_conf)
                if msg == self.DISCONNECT:
                    connection = False
                print(f'[{addr}] {msg}')

    def __send(self, client_conn: socket, msg: str) -> None:
        if not isinstance(msg, bytes):
            messege = msg.encode(self.FORMAT)
        else:
            messege = msg
        
        messege = msg.encode(self.FORMAT)
        msg_length = len(messege)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        client_conn.send(send_length)
        client_conn.send(messege)


    def start(self) -> None:
        print('[STARTING] server is starting...')
        self.server.listen()
        print(f'[LISTENING] server is listening on {self.SERVER}')
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.__handle_client, args=(conn, addr))
            thread.start()
            print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')

server_socket = Server()
server_socket.start()