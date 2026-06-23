class Fornecedor:
    def __init__(self, id, nome, telefone, especialidade):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.especialidade = especialidade

    def exibir_dados(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Especialidade: {self.especialidade}")

    def __str__(self):
        return f"Fornecedor(id={self.id}, nome='{self.nome}', telefone='{self.telefone}', especialidade='{self.especialidade}')"