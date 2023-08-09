import socket
import time

class server:
    def __init__(self):
        self.host='localhost'
        self.port=8001
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.log=open('logs.txt','a')
        self.users_credentials={'gui':'123'}
    
    def server_start(self):
        self.server_socket.bind((self.host,self.port))
        self.server_socket.listen()
        try:
            conn, addr= self.server_socket.accept()
            self.log.write(f'\n{addr[0]} : {time.asctime()}')
            self.log.close()

            while True:
                data=conn.recv(1024).decode()
                if not data:
                    raise 'NotData'
                else:

                    if data=='LOGIN':
                        login=conn.recv(1024).decode()
                        login_tuple=tuple(login.split(':')) 
                        
                        if (str(login_tuple[0]) in self.users_credentials) and (login_tuple[1]==self.users_credentials[str(login_tuple[0])]):
                            conn.send('LOGADO COM SUCESSO'.encode())
                            user_file=open(f'{login_tuple[0]}.txt','a')
                            while True:
                                resp=conn.recv(1024).decode()
                                resp_list=list(resp.split(':'))

                                if not resp:
                                    continue
                                
                                if resp_list[2]=='a':
                                    user_file.write(f'{str(resp_list[0])}:{str(resp_list[1])}')
                                    user_file.close()
                        else:
                            conn.send('USUÁRIO OU SENHA INCORRETOS'.encode())
                        
                    if data=='REGISTRAR':
                        login=conn.recv(1024).decode()
                        login_tuple=tuple(login.split(':'))
                        if login_tuple[0] not in self.users_credentials:
                            self.users_credentials.update({str(login_tuple[0]): str(login_tuple[1])})
                            conn.send('REGISTRADO COM SUCESSO'.encode())
                        else:
                            conn.send('USUÁRIO JÁ EXISTE'.encode())
                        print(self.users_credentials)
                
        except:
            pass
    
if __name__=='__main__':
    print('INICIANDO')
    server1=server()
    server1.server_start()