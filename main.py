import pyodbc
from classes.usuario import Usuario

#dados do banco
driver = "MySQL ODBC 9.7 ANSI Driver"
server = "localhost"
database = "revisoes_carro"
username = "root"
password = "545458"
port = 3306

# string de dados de conexao ao banco
dados_conexao = (
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"PORT={port};"
    f"DATABASE={database};"
    f"USER={username};"
    f"PASSWORD={password};"
    f"charset=utf8mb4;"
)

conexao = pyodbc.connect(dados_conexao)

def cadastro_usuario():
    novo_usuario = Usuario.coletar_dados()
    try:
        cursor = conexao.cursor()
        sql = """INSERT INTO usuarios (nome, email, telefone, senha)
                 VALUES (?, ?, ?, ?)"""
        cursor.execute(sql, (
            novo_usuario.nome,
            novo_usuario.email,
            novo_usuario.telefone,
            novo_usuario.senha
        ))
        conexao.commit()

        cursor.execute("SELECT LAST_INSERT_ID()")
        novo_usuario.id = cursor.fetchone()[0]

        print("\n Usuário cadastrado com sucesso!")
        novo_usuario.exibir_dados()
    except Exception as e:
        conexao.rollback()
        print(f"\n Erro ao cadastrar usuário: {e}")
 
 
def cadastro_veiculo():
    print("[ cadastro_veiculo ] - ainda não implementado")
 
 
def cadastro_tipo_manutencao():
    print("[ cadastro_tipo_manutencao ] - ainda não implementado")
 
 
def cadastro_novo_fornecedor():
    print("[ cadastro_novo_fornecedor ] - ainda não implementado")
 
 
def consulta_email():
    print("[ consulta_email ] - ainda não implementado")
 
 
def consulta_placa():
    print("[ consulta_placa ] - ainda não implementado")

tipo_cadastro = {           
    "1": cadastro_usuario,
    "2": cadastro_veiculo,
    "3": cadastro_tipo_manutencao,
    "4": cadastro_novo_fornecedor,
}
 
tipo_consultas = {
    "1": consulta_email,
    "2": consulta_placa,
}
def main():
 
    while True:
        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Cadastros")
        print("2 - Consultas")
        print("0 - Sair")
 
        opcao = input("Escolha: ").strip()
 
        if opcao == "0":
            print("Encerrando sistema...")
            break
 
        elif opcao == "1":
            print("\n========== MENU CADASTROS ==========")
            print("1 - Cadastro de novo usuário")
            print("2 - Cadastro de novo veículo")
            print("3 - Cadastro de novo tipo de manutenção")
            print("4 - Cadastro de novo fornecedor")
            print("0 - Retornar")
 
            tipo = input("Escolha: ").strip()
 
            if tipo == "0":
                continue
            elif tipo in tipo_cadastro:
                tipo_cadastro[tipo]()
            else:
                print("Opção inválida.")
 
        elif opcao == "2":
            print("\n========== MENU CONSULTAS ==========")
            print("1 - Consulta por E-mail (Usuário)")
            print("2 - Consulta por Placa (Veículo)")
            print("0 - Retornar")
 
            tipo = input("Escolha: ").strip()
 
            if tipo == "0":
                continue
            elif tipo in tipo_consultas:
                tipo_consultas[tipo]()
            else:
                print("Opção inválida.")
 
        else:
            print("Opção inválida.")

    
main()

