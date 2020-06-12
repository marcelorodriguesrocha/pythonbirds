class Pessoa:
    def __init__(self, *filhos, nome=None, idade= 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá Mundo{id(self)}'

if __name__ == '__main__':
    marcelo = Pessoa(nome='Marcelo')
    giovanna = Pessoa(marcelo, nome='Giovanna')
    print(Pessoa.cumprimentar(giovanna))
    print(id(giovanna))
    print(giovanna.cumprimentar())
    print(giovanna.nome)
    print(giovanna.idade)
    for filho in giovanna.filhos:
        print(filho.nome)
        giovanna.sobrenome= 'Rocha' # atributo dinamico foi feito depois dos atributos acima
        del giovanna.filhos
        print(giovanna.__dict__)
        print(marcelo.__dict__)
