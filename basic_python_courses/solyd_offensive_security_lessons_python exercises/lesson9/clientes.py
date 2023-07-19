class Cliente:
    def __init__(self, cpf, idade, nome):
        self. nome= nome
        self.cpf=cpf
        self.idade=idade

    def __str__(self):
        return self.nome