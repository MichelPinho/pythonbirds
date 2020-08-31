class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=44):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    @staticmethod
    def metodo_estatico():
        return 44

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'

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

    print(michel.olhos)
    print(renzo.olhos)
    print(Pessoa.metodo_estatico(), michel.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), michel.nome_e_atributos_de_classes())



