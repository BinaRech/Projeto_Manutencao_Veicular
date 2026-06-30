# ================================================= #
#  Classe Carro                                     #
#  Responsável por armazenar os dados dos veículos  #
#  cadastrados no sistema de manutenção veicular.   #
# ================================================= #

class Carro:

    # construtor da classe, inicializa os dados do veículo
    def __init__(self, placa, marca, modelo, ano, cor, km_atual, sinistro=False):

        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.km_atual = km_atual
        self.sinistro = sinistro

        # armazena o histórico de manutenções do veículo
        self.manutencoes = []


    # exibe todas as informações do veículo
    def exibir_dados(self):

        print("\n===== DADOS DO VEÍCULO =====\n")

        print(f"Placa: {self.placa}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"KM atual: {self.km_atual}")
        print(f"Sinistro: {'Sim' if self.sinistro else 'Não'}")

        print("\n============================\n")


    # utilizado pela classe Manutencao para vincular uma ao veículo
    def adicionar_manutencao(self, manutencao):
        self.manutencoes.append(manutencao)


    # atualiza a quilometragem do veículo
    def atualizar_km(self, novo_km):

        if novo_km > self.km_atual:
            self.km_atual = novo_km
        else:
            print("Erro: a quilometragem não pode diminuir.")


    # coleta os dados do veículo pelo terminal
    @staticmethod
    def coletar_dados():

        print("\n===== CADASTRO DE VEICULO =====")

        placa = input("Placa: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        cor = input("Cor: ")
        km_atual = int(input("KM atual: "))

        resposta = input("Possui sinistro? (s/n): ").lower()
        sinistro = resposta == "s"

        return Carro(
            placa,
            marca,
            modelo,
            ano,
            cor,
            km_atual,
            sinistro     
        )


    # retorna uma representação em texto do veículo
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"
