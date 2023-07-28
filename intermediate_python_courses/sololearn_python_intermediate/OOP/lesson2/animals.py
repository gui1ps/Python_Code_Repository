class Animal:
    def __init__(self,especie,legs,color,cutenesslevel):
        self.especie=especie
        self.legs=legs
        self.color=color
        self.cutnesslevel=cutenesslevel
    
    def show(self):
        print('I am a animal')
    
class Cat(Animal):
    def __init__(self,legs, color,name):
        super().__init__('Cat', legs, color, 10)
        self.name=name

    def show(self):
        print(f'''
              Hi, my name is {self.name} and I'm a {self.color} {self.especie}
        ฅ(ﾐ⚈ ﻌ ⚈ﾐ)ฅ
''')
class Dog(Animal):
    def __init__(self, legs, color,name):
        super().__init__('Dog', legs, color, 10)
        self.name=name
    
    def show(self):
        print(f'''
              Hi, my name is {self.name} and I'm a {self.color} {self.especie}
        (❍ᴥ❍ʋ)
''')

    
if __name__=="__main__":
    felix=Cat(4,'brown','Felix')
    jake=Dog(4,'Yellow','Jake')
    felix.show()
    jake.show()