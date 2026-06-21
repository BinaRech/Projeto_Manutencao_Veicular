class Carro:

    def __init__(self, placa, marca, modelo, ano, cor, km):

        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.km = km

    def exibir_dados(self):

        print("\n===== DADOS DO VEÍCULO =====")

        print(f"Placa: {self.placa}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"KM: {self.km}")

#isso é so pra testar o VScode