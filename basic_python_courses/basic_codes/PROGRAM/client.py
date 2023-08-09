import socket
class client:
    def __init__(self,hsot_to_connect,port_to_connect):
        self.client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host=hsot_to_connect
        self.port=port_to_connect
    
    def client_connect(self):
        try:
            self.client_socket.connect((self.host,self.port))
        except:
            print('error')