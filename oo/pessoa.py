class Pessoa:
    def __init__(self, nome=None, idade= 35):
        self.idade = idade
        self.nome = nome


    def cumprimentar(self):
        return f'Olá Mundo{id(self)}'

if __name__ == '__main__':
    p = Pessoa('giovanna')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Marcelo'
    print(p.nome)
    print(p.idade)