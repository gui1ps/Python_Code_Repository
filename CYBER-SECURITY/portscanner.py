import socket

resposta_n=False
port=[]
btfresult=[]

for num in range(65538):
        port.append(num)


pergunta=input("Deseja realizar um btfc?Y ou n ")

if pergunta=="n":
        resposta_n=True
        while resposta_n:
                dom=input("Dominio: ")
                porta=int(input("Porta:" ))

                client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.1)
                code=client.connect_ex((dom,porta))
                if code==0:
                        print("porta aberta")
                        continue
                else:
                        print(code)
                        continue

elif pergunta=="Y":
        dom=input("Dominio: ")

        for porta in port:
                client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.1)
                code=client.connect_ex((dom,porta))

                if code==0:
                        print("porta aberta: {}".format((porta)))
                        btfresult.append(porta)
                else:
                        print("porta fechada: {}".format((porta)))
        print(btfresult)            
