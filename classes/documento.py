# ================================================= #
#  Classe Documento                                 #
#  Responsável por armazenar documentos             #
#  relacionados a uma manutenção                    #
# ================================================= #

class Documento:

    # construtor da classe, inicializa os dados do docuemnto
    def __init__(self, id, revisao_id, nome_arquivo, caminho_arquivo):

        self.id = id
        self.revisao_id = revisao_id
        self.nome_arquivo = nome_arquivo
        self.caminho_arquivo = caminho_arquivo


    # exibe as informações do documento
    def exibir_dados(self):

        print("\n===== DOCUMENTO =====\n")

        print(f"ID: {self.id}")
        print(f"ID Revisão: {self.revisao_id}")
        print(f"Nome do arquivo: {self.nome_arquivo}")
        print(f"Caminho: {self.caminho_arquivo}")

        print("\n===========================\n")


    # atualiza o caminho do arquivo
    def alterar_caminho(self, novo_caminho):

        self.caminho_arquivo = novo_caminho


    # retorna uma representação em texto do documento
    def __str__(self):

        return f"{self.nome_arquivo}"
