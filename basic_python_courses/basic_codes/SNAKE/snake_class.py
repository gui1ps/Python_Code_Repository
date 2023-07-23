import random

class Snake:

    def __init__(self):
        self.position=None
    
    def setPosition(self,mapa):
        position=random.randint(1,(len(mapa)-2)),random.randint(1,(len(mapa[0])-2))
        if mapa[position[0]][position[1]]!=2:
            mapa[position[0]][position[1]]=3
            self.position=position
    
    def getPosition(self):
        return self.position
    
    def moverCima(self):
        self.position=pass
        
    


