class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá Mundo{id(self)}'

    @staticmethod  # metedo de classe
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):  # metedo de classe, para acessar metodos da propria classe
        return f' {cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    marcelo = Mutante(nome='Marcelo')
    giovanna = Homem(marcelo, nome='Giovanna')
    print(Pessoa.cumprimentar(giovanna))
    print(id(giovanna))
    print(giovanna.cumprimentar())
    print(giovanna.nome)
    print(giovanna.idade)
    for filho in giovanna.filhos:
        print(filho.nome)
    giovanna.sobrenome = 'Rocha'  # atributo dinamico foi feito depois dos atributos acima
    del giovanna.filhos
    print(giovanna.__dict__)
    print(marcelo.__dict__)
    print(Pessoa.olhos)
    print(giovanna.olhos)
    print(marcelo.olhos)
    print(id(Pessoa.olhos), id(giovanna.olhos), id(marcelo.olhos))
    print(Pessoa.metodo_estatico(), giovanna.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), giovanna.metodo_estatico())

    pessoa = Pessoa('anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(marcelo, Pessoa))
    print(isinstance(marcelo, Homem))
    print(marcelo, olhos)
