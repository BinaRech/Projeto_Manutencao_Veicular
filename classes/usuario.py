# ================================================= #
#  Classe Usuario                                   #
#  Responsável por armazenar os dados dos usuários  #
#  cadastrados no sistema                           #
# ================================================= #

class Usuario:

    # construtor da clase, inicializa os dados do usuário
    def __init__(self, id, nome, email, telefone, senha):

        self.id = id # usado no SQL
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha


    # exibe as informações do usuário(não exibir senha)
    def exibir_dados(self):

        print("\n===== DADOS DO USUÁRIO =====")

        print(f"ID:  {self.id}")
        print(f"Nome:  {self.nome}")
        print(f"Email:  {self.email}")
        print(f"Telefone:  {self.telefone}")

        print("\n===========================\n")

        # guarda os veículos cadastrado pelo usuario
        self.veiculos = []


    # adiciona um veículo a lista do usuário
    def adicionar_veiculo(self, veiculo):

        self.veiculo.append(veiculo)    


    # atualiza o email do usuario
    def alterar_email(self, novo_email):

        self.email = novo_email


    # atualiza o telefone do usuario
    def alterar_telefone(self, novo_telefone):

        self.telefone = novo_telefone


    # retorna uma representação em texto do usuário
    def __str__(self):

        return f"{self.nome} - {self.email}"

    