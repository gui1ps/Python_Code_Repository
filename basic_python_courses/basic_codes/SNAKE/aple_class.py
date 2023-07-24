import random
class Aple:
    def __init__(self):
        self.position=None
    
    def setPosition(self,mapa):
        positions=random.randint(1,(len(mapa)-2)),random.randint(1,(len(mapa[0])-2))
        self.position=list(positions)
        if mapa[self.position[0]][self.position[1]]!=3:
            mapa[self.position[0]][self.position[1]]=2

                   