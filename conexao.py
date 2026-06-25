import mysql.connector

#dados do banco
host = "reseau.proxy.rlwy.net"
database = "railway"
user = "root"
senha = "yHXwDGsbPmjfjPfepYYtKZlOdMtmYvxL"
port = 34141

def conecta():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=senha,
        database=database,
        port=port,
        charset="utf8mb4"
    )
