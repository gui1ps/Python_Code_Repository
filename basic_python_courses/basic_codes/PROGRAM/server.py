import socket
class server:
    def __init__(self):
        self.host='localhost'
        self.port=8000
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def server_start(self):
        self.server_socket.bind((self.host,self.port))
        self.server_socket.listen()
        try:
            conn, addr= self.server_socket.accept()
            print(f'CONECTADO: {addr}')
        except:
            print('error')