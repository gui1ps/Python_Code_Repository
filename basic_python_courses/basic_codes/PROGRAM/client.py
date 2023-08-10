import socket

class client:
    def __init__(self,hsot_to_connect,port_to_connect):
        self.client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host=hsot_to_connect
        self.port=port_to_connect
        self.conn_flag=False
    
    def change_login_status(self,boolean):
        self.conn_flag=bool(boolean)

    def client_connect(self):
        try:
            self.client_socket.connect((self.host,self.port))
            return True
        except:
            return False

if __name__=='__main__':
    client1=client('localhost',8001)
    if client1.client_connect():
        conn_flag=True
        print('CONECTADO\n')
    else:
        print('Algum erro ocorreu')
    
    while conn_flag:

        print('LOGIN\nREGISTRAR')
        response=input(">>").upper()

        if response=='LOGIN':
            client1.client_socket.send(response.encode())
            user_name=input("USER: ")
            user_pass=input("PASSWORD: ")
            resp=f'{user_name}:{user_pass}'
            client1.client_socket.send(resp.encode())

            try:
                server_response=client1.client_socket.recv(1024).decode()
            except:
                print('Problemas com o servidor'.upper())
                continue

            print(server_response)
            if server_response=='LOGADO COM SUCESSO':
                while True:
                    action=int(input('''
                        ADICIONAR NO ESTOQUE [0]
                         VER ITENS DO ESTOQUE[1]
                                         SAIR[2]
                            >>'''))
                    
                    if action==0:
                        iten=input('name: ')
                        qnt=input('qnt: ')
                        resp=f'{iten}:{qnt}:a'
                        client1.client_socket.send(resp.encode())
                    
                    if action==1:
                        client1.client_socket.send('r'.encode())
                        server_response=client1.client_socket.recv(1024).decode()
                        print(server_response)
                    
                    if action==2:
                        break
            else:
                continue
        
        if response=='REGISTRAR':
            client1.client_socket.send(response.encode())
            user_name=input("USER: ")
            user_pass=input("PASSWORD: ")
            resp=f'{user_name}:{user_pass}'
            client1.client_socket.send(resp.encode())

            try:
                server_response=client1.client_socket.recv(1024).decode()
            except:
                print('Problemas com o servidor'.upper())
                continue

            print(server_response)
            continue