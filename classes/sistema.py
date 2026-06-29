# ================================================= #
#  Classe Sistema                                   #
#  Responsável pelas regras de negócio do sistema   #
#  e pelas integrações externas (Telegram, SQL).    #
# ================================================= #

import requests
from conexao import conecta
from datetime import date
from funcoes_banco import buscar_telegram_id, buscar_telegram_por_placa

class Sistema:

    # construtor da classe
    def __init__(self):

        # dias antes da revisão para enviar notificações
        self.dias_notificacao = [30, 15, 7, 1]

        # token do bot do Telegram
        self.token_telegram = "8821945772:AAHv8FejJiq-ElB4UtoQcCAxQEUS9fQHnpg"

    # verifica quais manutencoes precisam de alerta
    def verificar_manutencoes_pendentes(self):

        conexao = conecta()
        cursor = None

        try:
            cursor = conexao.cursor()

            sql = """
            SELECT placa, data_revisao
            FROM manutencao
            """

            cursor.execute(sql)
            manutencoes = cursor.fetchall()

            hoje = date.today()

            for manutencao in manutencoes:
                placa = manutencao[0]
                data_revisao = manutencao[1]

                dias_restantes = (data_revisao - hoje).days

                if dias_restantes in self.dias_notificacao or dias_restantes == 0:

                    mensagem = (
                        "🚗🔔 DriveAlert System\n\n"
                        "Olá!\n\n"
                        f"Seu veículo {placa} possui uma manutenção programada.\n\n"
                        f"📅 Data da revisão: {data_revisao}\n"
                        f"⏳ Dias restantes: {dias_restantes}\n\n"
                    )   

                    if dias_restantes == 0:
                        mensagem += "⚠️ A revisão deve ser realizada hoje!\n\n"

                    elif dias_restantes == 1:
                        mensagem += "⚠️ A revisão será amanhã!\n\n"

                    else:
                        mensagem += "Lembre-se de agendar sua manutenção.\n\n"

                    mensagem += "Equipe DriveAlert 🚗"

                    telegram_id = buscar_telegram_por_placa(placa)

                    if telegram_id:
                        self.enviar_notificacao(telegram_id, mensagem)
                    else:
                        print("Telegram ID do proprietário não encontrado.")

        except Exception as e:
            print(f"Erro: {e}")

        finally:
            if cursor:
                cursor.close()
            conexao.close()

    # envia uma notificacao para um usuario
    def enviar_notificacao(self, telegram_id, mensagem):

        url = f"https://api.telegram.org/bot{self.token_telegram}/sendMessage"

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
