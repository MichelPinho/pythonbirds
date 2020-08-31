class Pessoa:
    def __init__(self, *filhos, nome=None, idade=44):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':

    renzo = Pessoa(nome='Renzo')
    michel = Pessoa(renzo, nome='Michel')
    print(Pessoa.cumprimentar(michel))
    print(michel.cumprimentar())
    print(michel.nome)
    print(michel.idade)
    for filho in michel.filhos:
        print(filho.nome)
