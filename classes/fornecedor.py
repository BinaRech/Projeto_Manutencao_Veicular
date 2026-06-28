class Fornecedor:
    def __init__(self, nome, telefone, especialidade, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.especialidade = especialidade

    def __str__(self):
        return self.nome
    

    def exibir_dados(self):

        print("\n===== FORNECEDOR =====\n")

        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Especialidade: {self.especialidade}")

        print("\n======================\n")

    

    @staticmethod
    def coletar_dados():

        print("\n=== Cadastro de Fornecedor ===")

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        especialidade = input("Especialidade: ")


        return Fornecedor(
            nome,
            telefone, 
            especialidade
            )


