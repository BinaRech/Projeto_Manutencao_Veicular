# ================================================= #
#  Classe Sistema                                   #
#  Responsável pelas regras de negócio do sistema   #
#  e pelas integrações externas (Telegram, SQL).    #
# ================================================= #

import requests
from funcoes_banco import buscar_telegram_id

class Sistema:

    # construtor da classe
    def __init__(self):

        # dias antes da revisão para enviar notificações
        self.dias_notificacao = [30, 15, 7, 1]

        # token do bot do Telegram
        self.toke_telegram = "8821945772:AAEO2Z35vmkEjc6TPIb0ts3q35iHrH8NYzw"

    # verifica quais manutencoes precisam de alerta
    def verificar_manutencoes_pendentes(self):

        print("Função ainda não implementada")

    # envia uma notificacao para um usuario
    def enviar_notificacao(self, telegram_id, mensagem):
   
        url = ( 
            f"https://api.telegram.org/"
            f"bot{self.toke_telegram}/sendMessage"
        )

        dados = {
            "chat_id": telegram_id,
            "text": mensagem
        }

        try:
            resposta = requests.post(url, data=dados)

            if resposta.status_code == 200:
                print("Notificação enviada com sucesso!")
            else:
                print("Erro ao enviar notificação.")
                print(resposta.json())
        except Exception as e:
            print(f"Erro de conexão com o Telegram: {e}")


    # busca o telegram_id pelo e-mail e envia uma notificação
    def enviar_notificacao_por_email(self, email, mensagem):

        telegram_id = buscar_telegram_id(email)

        if telegram_id:
            self.enviar_notificacao(telegram_id, mensagem)
        else:
            print("Não foi possível encontrar o Telegram do usuário!")
