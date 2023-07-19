class clients:
    def __init__(self,name,password):
        self.name=name
        self.password=password

    def getPass(self):
        return str(self.password)
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return'\n CLIENT NAME: ',self.name,'\nCLIENTE PASSWORD: ',self.password