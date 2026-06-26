# ================================================= #
#  Classe Sistema                                   #
#  Responsável pelas regras de negócio do sistema   #
#  e pelas integrações externas (Telegram, SQL).    #
# ================================================= #

class Sistema:

    # construtor da classe
    def __init__(self):

        # dias antes da revisão para enviar notificações
        self.dias_notificacao = [30, 15, 7, 1]

    # verifica quais manutencoes precisam de alerta
    def verificar_manutencoes_pendentes(self):

        print("Função ainda não implementada")

    # envia uma notificacao para um usuario
    def enviar_notificacao(self, telegram_id, mensagem):

        print("Função ainda não implementada")

    # consulta um usuário pelo email
    def consultar_usuario_email(self, email):

        print("Função ainda não implementada")

    # consulta um veiculo pela placa
    def consultar_veicula_placa(self, placa):

        print("Função ainda não implementada")