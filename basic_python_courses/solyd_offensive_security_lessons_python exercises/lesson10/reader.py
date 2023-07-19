from arquivo import Arquivo

class Writer:
    def __init__(self,arquivo,metodo):
        self.path=arquivo.path
        self.metodo=metodo
        self.arquivo=''

    def escrever(self,msg):
        with open (self.path,self.metodo,encoding='utf-8') as self.arquivo:
            self.arquivo.write(msg)

if __name__=="__main__":
    arquivo1=Arquivo('arquivo.txt')
    escritor=Writer(arquivo1,'a')
    escritor2=Writer(arquivo1,'a')
    escritor.escrever("\n1")
    escritor2.escrever('\n2')
    