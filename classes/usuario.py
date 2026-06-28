# ================================================= #
#  Classe Usuario                                   #
#  Responsável por armazenar os dados dos usuários  #
#  cadastrados no sistema                           #
# ================================================= #

class Usuario:

    # construtor da classe, inicializa os dados do usuário
    def __init__(self, id, nome, email, telefone, senha, telegram_id=None):

        self.id = id # usado no SQL
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.telegram_id = telegram_id

        # guarda os veículos cadastrados pelo usuario
        self.veiculos = []


    # exibe as informações do usuário(não exibir senha)
    def exibir_dados(self):

        print("\n===== DADOS DO USUÁRIO =====")

        print(f"ID:  {self.id}")
        print(f"Nome:  {self.nome}")
        print(f"Email:  {self.email}")
        print(f"Telefone:  {self.telefone}")
        print(f"Telegram ID:  {self.telegram_id}")

        print("\n===========================\n")


    # adiciona um veículo a lista do usuário
    def adicionar_veiculo(self, veiculo):

        self.veiculos.append(veiculo)    


    # atualiza o email do usuário
    def alterar_email(self, novo_email):

        self.email = novo_email


    # atualiza o telefone do usuário
    def alterar_telefone(self, novo_telefone):

        self.telefone = novo_telefone

    
    @staticmethod
    def coletar_dados():
 
        print("\n===== CADASTRO DE USUÁRIO =====")
        nome = input("Nome:     ")
        email = input("Email:    ")
        telefone = input("Telefone: ")
        telegram_id = int(input("Telegram Id: "))
        senha = input("Senha:    ")
 
        # id=None porque o banco gera o ID automaticamente (AUTO_INCREMENT)
        return Usuario(
            id=None,
            nome=nome,
            email=email,
            telefone=telefone,
            telegram_id=telegram_id,
            senha=senha
            )
 
 
    # retorna uma representação em texto do usuário
    def __str__(self):
 
        return f"{self.nome} - {self.email}"

    