import random

class NumberForGame:
    def __init__(self):
        self.initial_range=random.randint(0,10)
        self.final_range=random.randint(12,20)
        self.value=random.randint(self.initial_range,self.final_range)

    def getIR(self):
        return self.initial_range

    def getFR(self):
        return self.final_range

    def dardicadificil(self):
        return (self.initial_range,self.final_range)
    
    def dardicamedia(self):
        media_do_range=(self.final_range-self.initial_range)/2
        if self.value>=media_do_range:
            return self.final_range
        else:
            return self.initial_range
    
    def dardicafacil(self):
        if (self.value+1)<self.final_range:
            return(self.value+1)
        elif(self.value-1)>self.initial_range:
            return(self.value-1)
        
    def entregarojogo(self):
        return self.value
    
    def __str__(self):
        return f'RI {self.initial_range} \nRF: {self.final_range}\nVALOR: {self.value}'
    

if __name__=='__main__':
    '''
    valor1=NumberForGame()
    print(valor1.__str__())
    print(str(valor1.dardicadificil()))
    print(str(valor1.dardicamedia()))
    print(str(valor1.dardicafacil()))
    print(str(valor1.entregarojogo()))
    '''