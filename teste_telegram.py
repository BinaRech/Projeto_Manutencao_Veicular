import requests

TOKEN = "8821945772:AAEO2Z35vmkEjc6TPIb0ts3q35iHrH8NYzw"
CHAT_ID = 6793888860

mensagem = "🚗 DriveAlert System funcionando com sucesso!"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

dados = {
    "chat_id": CHAT_ID,
    "text": mensagem
}

resposta = requests.post(url, data=dados)

print(resposta.json())