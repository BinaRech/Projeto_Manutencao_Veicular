# ================================================= #
#  Classe Sistema                                   #
#  Responsável pelas regras de negócio do sistema   #
#  e pelas integrações externas (Telegram, SQL).    #
# ================================================= #

import requests
from conexao import conecta
from datetime import date, timedelta
from funcoes_banco import buscar_telegram_id, buscar_telegram_por_placa

class Sistema:

    # construtor da classe
    def __init__(self):

        # dias antes da revisão para enviar notificações
        self.dias_notificacao = [30, 15, 7, 1]

        # margem de quilometragem para envio de alerta
        self.km_notificacao = 1000

        # token do bot do Telegram
        self.token_telegram = "8821945772:AAHv8FejJiq-ElB4UtoQcCAxQEUS9fQHnpg"

    # verifica quais manutencoes precisam de alerta
    def verificar_manutencoes_pendentes(self):

        conexao = conecta()
        cursor = None

        try:
            cursor = conexao.cursor()

            # consulta a última manutenção registrada de cada tipo para cada veículo,
            # obtendo também os intervalos de revisão e a quilometragem atual
            # para verificar se é necessário enviar um alerta ao proprietário
            sql = """
            SELECT 
                m.placa,
                m.data_revisao,
                m.km_atual,
                t.nome,
                t.intervalo_km,
                t.intervalo_meses,
                c.km_atual
            FROM manutencao m
            INNER JOIN carros c
                ON c.placa = m.placa
            INNER JOIN tipo_manutencao t
                ON t.id = m.tipo_revisao_id
            INNER JOIN (
                SELECT
                    placa,
                    tipo_revisao_id,
                    MAX(data_revisao) AS ultima_data
                FROM manutencao
                GROUP BY placa, tipo_revisao_id
            ) ult
                ON ult.placa = m.placa
                AND ult.tipo_revisao_id = m.tipo_revisao_id
                AND ult.ultima_data = m.data_revisao
            """

            cursor.execute(sql)
            manutencoes = cursor.fetchall()

            # data atual usada para calcular os dias restantes
            hoje = date.today()

            # percorre as manutenções encontradas
            for manutencao in manutencoes:
                placa = manutencao[0]
                data_manutencao = manutencao[1]
                km_manutencao = manutencao[2]
                nome_tipo = manutencao[3]
                intervalo_km = manutencao[4]
                intervalo_meses = manutencao[5]
                km_atual_carro = manutencao[6]

                 # variáveis usadas nos cálculos
                proxima_data = None
                proxima_km = None
                dias_restantes = None
                km_restantes = None

                # calcula a próxima revisão por tempo
                # usando a data da última manutenção + intervalo em meses
                if intervalo_meses is not None:
                    proxima_data = data_manutencao + timedelta(days=intervalo_meses * 30)
                    dias_restantes = (proxima_data - hoje).days

                # calcula a próxima revisão por quilometragem
                # usando o KM da última manutenção + intervalo em KM
                if intervalo_km is not None:
                    proxima_km = km_manutencao + intervalo_km
                    km_restantes = proxima_km - km_atual_carro

                # verifica se a manutenção está próxima pela data
                alerta_por_data = (
                    dias_restantes is not None
                    and (dias_restantes in self.dias_notificacao or dias_restantes == 0)
                )

                # verifica se a manutenção está próxima pela quilometragem
                alerta_por_km = (
                    km_restantes is not None
                    and km_restantes <= self.km_notificacao
                )

                # se houver alerta por data ou por km, monta a mensagem
                if alerta_por_data or alerta_por_km:

                    # mensagem enviada ao proprietário pelo Telegram
                    mensagem = (
                        "🚗🔔 DriveAlert System\n\n"
                        "Olá!\n\n"
                        f"Seu veículo {placa} possui uma manutenção próxima.\n\n"
                        f"🔧 Serviço: {nome_tipo}\n"
                        f"📅 Última manutenção: {data_manutencao}\n"
                    )

                    if proxima_data is not None:
                        mensagem += f"📆 Próxima revisão por tempo: {proxima_data}\n"
                        mensagem += f"⏳ Dias restantes: {dias_restantes}\n"

                    if proxima_km is not None:
                        mensagem += f"🛣️ Próxima revisão por KM: {proxima_km:,} km\n".replace(",", ".")
                        mensagem += f"📍 KM atual do veículo: {km_atual_carro:,} km\n".replace(",", ".")
                        mensagem += f"⏱️ KM restantes: {km_restantes:,} km\n".replace(",", ".")

                    mensagem += "\n"

                    if dias_restantes == 0:
                        mensagem += "⚠️ A revisão deve ser realizada hoje!\n\n"
                    elif dias_restantes == 1:
                        mensagem += "⚠️ A revisão será amanhã!\n\n"
                    elif alerta_por_data:
                        mensagem += "Lembre-se de agendar sua manutenção.\n\n"

                    if km_restantes is not None and km_restantes <= 0:
                        mensagem += "⚠️ A revisão já atingiu ou passou da quilometragem recomendada!\n\n"
                    elif alerta_por_km:
                        mensagem += "⚠️ A revisão está próxima pela quilometragem!\n\n"

                    mensagem += "Equipe DriveAlert 🚗"

                    # busca o Telegram ID do proprietário do veículo
                    telegram_id = buscar_telegram_por_placa(placa)

                    # envia a notificação caso o Telegram ID exista
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
