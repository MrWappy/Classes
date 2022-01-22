class Pessoa():
    def __init__(self, fname, lname, age=None):
        self.nome = fname
        self.apelido = lname
        self.idade = age


class Professor(Pessoa):
    def __init__(self, unidades, fname, lname):
        super().__init__(fname, lname)
        self.disciplinas = unidades
        self._horario = []

    def add_horario(self, dia):
        for i in dia:
            self._horario.append(i)

    def get_horario(self):
        return self._horario

class Engenheiro(Pessoa):
    def __init__(self, esp, **kwargs):
        super().__init__(**kwargs)
        self.colegio = esp




'''
t = Professor(["AED", "ICC"], "João", "Mendes")
print(f"{t.nome} {t.apelido} - {t.idade} - {t.disciplinas} - {t._horario}")
t.idade = 18
print(t.idade)
t.add_horario(["Quarta", "Sábado"])
print(t.get_horario())
for idx, i in enumerate(t.get_horario()):
    print(idx, "-", i)
e = Engenheiro("Informática", fname="José",age=30,lname="laranja")
print(e.colegio)
print(e.nome + " " + e.apelido)
'''
#--------------------------------------//-----------------------------//----------------------------------------

class Artigo():
    def __init__(self, id, nome, preço):
        self.id = id
        self.nome = nome
        self.preço = preço

    def gravar(self, nome, preço):
        self.nome = nome
        self.preço = preço


class Congelados(Artigo):
    def __init__(self, tipo, **kwargs):
        super().__init__(**kwargs)
        self.tipo = tipo


class Bebidas(Artigo):
    def __init__(self, capacidade, **kwargs):
        super().__init__(**kwargs)
        self.capacidade = capacidade

    def get_capacidade(self):
        return self.capacidade

'''
a = Artigo(id=1, nome="Laranja", preço="0.30€")
c = Congelados(id=2, nome="Costeletas de Porco", preço="2.50€", tipo="carne")
b = Bebidas(id=3, nome="Ice-Tea", preço="1€", capacidade="1.5L")


print("---------------------Bem Vindo Ao Supermercado--------------------------")
print(f"Artigo: nome-{a.nome} preço-{a.preço} id-{a.id}")
print(f"Congelado: nome-{c.nome} preço-{c.preço} id-{c.id} tipo-{c.tipo}")
print(f"Bebida: nome-{b.nome} preço-{b.preço} id-{b.id} capacidade-{b.get_capacidade()}")
a.gravar("Maçã", "0,26€")
print(a.nome)
print(a.preço)
print("----------------------------------------------------------------------")
'''