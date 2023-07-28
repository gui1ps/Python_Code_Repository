class Carro:
    def __init__(self, cor, marca, modelo):
        self.cor=cor
        self.marca=marca
        self.modelo=modelo

    def show(self):
        return f'I am a {self.modelo} from {self.marca} and my color is {self.cor}'

if __name__=='__main__':
    newcar = Carro('verde', 'mercedes','c180')
    print(newcar.show())