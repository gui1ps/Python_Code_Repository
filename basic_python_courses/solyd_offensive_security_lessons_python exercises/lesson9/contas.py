from clientes import Cliente
class conta:
    def __init__(self,Cliente,saldo,limite) :
        self.cliente=Cliente
        self.saldo=saldo
        self.limite=limite
    
    def depositar(self,valor):
        self.saldo+=valor
    
    def consulta_saldo(self):
        return self.saldo
    
    def sacar(self,valor):
        
        if valor>(self.saldo+self.limite):
            print('Erro: saldo insuficiente')
        else:
            self.saldo-=valor