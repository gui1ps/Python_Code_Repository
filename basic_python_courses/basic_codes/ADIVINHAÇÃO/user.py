class User:

    def __init__(self,user_name):
        self.user_name=user_name
        self.point=0
    
    def add_point(self):
        self.point+=5
    
    def sub_point(self):
        self.point-=2.5

    def getName(self):
        return self.user_name
    
    def getPoints(self):
        return self.point
    
    def setPoint(self,new_points):
        self.point=new_points

    def __str__(self) :
        return f'Usuário: {self.getName()} \nPontuação atual: {self.getPoints()}'