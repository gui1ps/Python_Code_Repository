import random


class Snake:
    def __init__(self):
        self.position=None
        self.body_positions=[]
        self.pontos=0
        self.live=True
    
    def setPosition(self,mapa):
        positions=random.randint(1,(len(mapa)-2)),random.randint(1,(len(mapa[0])-2))
        self.position=list(positions)
        mapa[self.position[0]][self.position[1]]=3

  
    def getPosition(self):
        return self.position
    
    def moverCima(self,mapa):
        self.position[0]-=1
        if mapa[self.position[0]][self.position[1]]==2:
            self.pontos+=1
            mapa[self.position[0]][self.position[1]]=3
        elif mapa[self.position[0]][self.position[1]]==1 or mapa[self.position[0]][self.position[1]]==3:
            self.live=False
        else:
           mapa[self.position[0]][self.position[1]]=3
           
    
    def moverBaixo(self,mapa):
        self.position[0]+=1
        if mapa[self.position[0]][self.position[1]]==2:
            self.pontos+=1
            mapa[self.position[0]][self.position[1]]=3
        elif mapa[self.position[0]][self.position[1]]==1 or mapa[self.position[0]][self.position[1]]==3:
            self.live=False
        else:
           mapa[self.position[0]][self.position[1]]=3
    
    def moverEsquerda(self,mapa):
        self.position[1]-=1
        if mapa[self.position[0]][self.position[1]]==2:
            self.pontos+=1
            mapa[self.position[0]][self.position[1]]=3
        elif mapa[self.position[0]][self.position[1]]==1 or mapa[self.position[0]][self.position[1]]==3:
            self.live=False
        else:
           mapa[self.position[0]][self.position[1]]=3
    
    def moverDireita(self,mapa):
        self.position[1]+=1
        if mapa[self.position[0]][self.position[1]]==2:
            self.pontos+=1
            mapa[self.position[0]][self.position[1]]=3
        elif mapa[self.position[0]][self.position[1]]==1 or mapa[self.position[0]][self.position[1]]==3:
            self.live=False
        else:
           mapa[self.position[0]][self.position[1]]=3
    
    


