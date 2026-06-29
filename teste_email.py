from classes.sistema import Sistema

sistema = Sistema()

sistema.enviar_notificacao_por_email(
    "teste@gmail.com",
    "🚗🔔 Teste automático do DriveAlert System!"
)