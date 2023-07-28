class Acount:
    def __init__(self,number,name,value):
        self.limite=1000
        self.__number=number
        self.__name=name
        self.__value=value

    def depositar(self,val):
        self.__value+=val
    
    def sacar(self,val):
        if val<=(self.__value+self.limite):
            self.__value-=val
        else:
            return False
    
    def get_number(self):
        return self.__number
    
    def get_name(self):
        return self.__name
    
    def get_value(self):
        return self.__value

    def tranferir(self,other,value):
        self.sacar(value)
        other.depositar(value)
    
    def __str__(self):
        return f'''
        {self.__number}
        {self.__name}
        {self.__value}
        '''

if __name__=="__main__":
    ac1=Acount('111-2','James',115)
    ac2=Acount('111-3','Juan',300)
    print(ac1.__str__())
    print(ac2.__str__())
    ac1.depositar(15)
    ac2.depositar(30)
    print(ac1.__str__())
    print(ac2.__str__())
    ac1.sacar(15)
    ac2.sacar(30)
    print(ac1.__str__())
    print(ac2.__str__())
    ac2.tranferir(ac1,20)
    print(ac1.__str__())
    ac1.tranferir(ac2,5)
    print(ac1.__str__())
    print(ac1.get_number())