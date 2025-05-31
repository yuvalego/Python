import socket 
import threading
import pickle

class Server:
    def __init__(self):
        self.PORT: int = 5050
        self.SERVER: str = socket.gethostbyname(socket.gethostname())
        self.ADDR: tuple = self.SERVER, self.PORT
        self.FORMAT: str = 'utf-8'
        self.DISCONNECT: str = 'QUIT'

        self.server: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

    def start(self) -> None:
        print('[STARTING] server is starting...')
        self.server.listen()
        print(f'[LISTENING] server is listening on {self.SERVER}')
        active_clients = 0
        max_clients = 5
        while active_clients < max_clients:
            conn, addr = self.server.accept()
            conv: threading.Thread = threading.Thread(target=self.__handle_client, args=(conn, addr))
            conv.start()
            active_clients = threading.active_count() - 1
            print(f'[ACTIVE CONNECTIONS] {active_clients}')

    def __handle_client(self, conn: socket, addr: str) -> None:
        print(f'[NEW CONNECTION] {addr} connected.')
        connection = True
        while connection:
            name, content = pickle.loads(self.__recv_data(conn))
            with open(f'database/{name}', 'wb') as file:
                file.write(content) 

    def __recv_data(self, conn: socket):
        full_data = bytearray()
        while (chunk := conn.recv(1024)):
            full_data.extend(chunk)
        return full_data

server = Server()
server.start()