class TipoManutencao:
    def __init__(self, id, nome, descricao, intervalo_km=None, intervalo_meses=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.intervalo_km = intervalo_km
        self.intervalo_meses = intervalo_meses

    def exibir_dados(self):

        print("\n===== TIPO DE MANUTENÇÃO =====\n")

        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")

        if self.intervalo_km:
            print(f"Intervalo: {self.intervalo_km} km")

        if self.intervalo_meses:
            print(f"Periodicidade: {self.intervalo_meses} meses")

        print("\n==============================\n")

    @staticmethod
    def coletar_dados():
        print("\n===== CADASTRO DE TIPO DE MANUTENÇÃO =====\n")

        nome = input("Nome: ")
        descricao = input("Descrição: ")
        #input em string para permitir vazio sem dar erro
        intervalo_km_input = input("Intervalo em KM: ")
        intervalo_km = int(intervalo_km_input) if intervalo_km_input.strip() else None
        #input em string para permitir vazio sem dar erro
        intervalo_meses_input = input("Intervalo em meses: ")
        intervalo_meses = int(intervalo_meses_input) if intervalo_meses_input.strip() else None

        return TipoManutencao(
            id=None,
            nome=nome,
            descricao=descricao,
            intervalo_km=intervalo_km,
            intervalo_meses=intervalo_meses
        )

    def __str__(self):
        return f"TipoManutencao({self.id}, {self.nome})"

    def __repr__(self):
        return self.__str__()