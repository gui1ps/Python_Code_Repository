import random

class Snake:
    def __init__(self):
        self.position=None
        self.body_positions=[]
        self.old_position=[]
        self.pontos=0
        self.live=True
    
    def setPosition(self,mapa):
        positions=random.randint(1,(len(mapa)-2)),random.randint(1,(len(mapa[0])-2))
        self.position=list(positions)
        mapa[self.position[0]][self.position[1]]=3

    def getPosition(self):
        return self.position
    
    def getOldPostion(self):
        return self.old_position
    
    def getBody(self):
        return self.body_positions
    
    def getPoints(self):
        return self.pontos

    def moverCima(self,mapa):
        self.old_position=self.getPosition()[0],self.getPosition()[1]
        if self.pontos>0:
            self.body_positions.append(list(self.old_position))
        self.position[0]-=1

        if [self.old_position[0],self.old_position[1]] not in self.body_positions:
            mapa[self.old_position[0]][self.old_position[1]]=0
        else:
            mapa[self.old_position[0]][self.old_position[1]]=3

        if mapa[self.position[0]][self.position[1]]==2:
            self.pontos+=1
            mapa[self.position[0]][self.position[1]]=3
        elif mapa[self.position[0]][self.position[1]]==1 or mapa[self.position[0]][self.position[1]]==3:
            self.live=False
        else:
         mapa[self.position[0]][self.position[1]]=3
           
    def moverBaixo(self,mapa):
        self.old_position=self.getPosition()[0],self.getPosition()[1]
        if self.pontos>0:
            self.body_positions.append(list(self.old_position))
        self.position[0]+=1

        if [self.old_position[0],self.old_position[1]] not in self.body_positions:
            mapa[self.old_position[0]][self.old_position[1]]=0
        else:
            mapa[self.old_position[0]][self.old_position[1]]=3

        if mapa[self.position[0]][self.position[1]]==2:
            self.pontos+=1
            mapa[self.position[0]][self.position[1]]=3
        elif mapa[self.position[0]][self.position[1]]==1 or mapa[self.position[0]][self.position[1]]==3:
            self.live=False
        else:
            mapa[self.position[0]][self.position[1]]=3
            
    def moverEsquerda(self,mapa):
        self.old_position=self.getPosition()[0],self.getPosition()[1]
        if self.pontos>0:
            self.body_positions.append(list(self.old_position))
        self.position[1]-=1

        if [self.old_position[0],self.old_position[1]] not in self.body_positions:
            mapa[self.old_position[0]][self.old_position[1]]=0
        else:
            mapa[self.old_position[0]][self.old_position[1]]=3

        if mapa[self.position[0]][self.position[1]]==2:
            self.pontos+=1
            mapa[self.position[0]][self.position[1]]=3
        elif mapa[self.position[0]][self.position[1]]==1 or mapa[self.position[0]][self.position[1]]==3:
            self.live=False
        else:
           mapa[self.position[0]][self.position[1]]=3
    
    def moverDireita(self,mapa):
        self.old_position=self.getPosition()[0],self.getPosition()[1]
        if self.pontos>0:
            self.body_positions.append(list(self.old_position))
        self.position[1]+=1

        if [self.old_position[0],self.old_position[1]] not in self.body_positions:
            mapa[self.old_position[0]][self.old_position[1]]=0
        else:
            mapa[self.old_position[0]][self.old_position[1]]=3

        if mapa[self.position[0]][self.position[1]]==2:
            self.pontos+=1
            mapa[self.position[0]][self.position[1]]=3
        elif mapa[self.position[0]][self.position[1]]==1 or mapa[self.position[0]][self.position[1]]==3:
            self.live=False
        else:
           mapa[self.position[0]][self.position[1]]=3
    
    


