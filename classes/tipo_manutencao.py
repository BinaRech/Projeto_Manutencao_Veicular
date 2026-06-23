class TipoManutencao:
    def __init__(self, id, nome, descricao, periodicidade_meses=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.periodicidade_meses = periodicidade_meses

    def exibir_dados(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        if self.periodicidade_meses:
            print(f"Periodicidade: {self.periodicidade_meses} meses")

    def __str__(self):
        return f"TipoManutencao({self.id}, {self.nome})"

    def __repr__(self):
        return self.__str__()