from conexao import conecta
from classes.usuario import Usuario
from classes.carro import Carro
from classes.tipo_manutencao import TipoManutencao
from classes.fornecedor import Fornecedor


conexao = None


def cadastro_usuario():
    novo_usuario = Usuario.coletar_dados()
    conexao = conecta()
    try:
        cursor = conexao.cursor()

        sql = """
        INSERT INTO usuarios (nome, email, telefone, senha)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (
            novo_usuario.nome,
            novo_usuario.email,
            novo_usuario.telefone,
            novo_usuario.senha
        ))

        conexao.commit()
        novo_usuario.id = cursor.lastrowid #serve para pegar o id que é gerado no banco
        print("\n Usuário cadastrado!")
        novo_usuario.exibir_dados()

    except Exception as e:
        conexao.rollback()
        print(f"\n Erro ao cadastrar usuário: {e}")

    finally:
        cursor.close()
        conexao.close()


def cadastro_veiculo():

    cursor = None
    conexao = None

    usuario_id = consulta_email()

    if usuario_id is None:
        print("\nCadastro de veículo cancelado: proprietário não encontrado.")
        return
    novo_carro = Carro.coletar_dados()
    conexao = conecta()

    try:
        cursor = conexao.cursor()

        sql = """
        INSERT INTO carros
        (placa, marca, modelo, ano, cor, km_atual, sinistro, usuario_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            novo_carro.placa,
            novo_carro.marca,
            novo_carro.modelo,
            novo_carro.ano,
            novo_carro.cor,
            novo_carro.km_atual,
            novo_carro.sinistro,
            usuario_id
        ))

        conexao.commit()

        print("Veículo cadastrado com sucesso!")

        novo_carro.exibir_dados()

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao cadastrar veículo:  {e}")

    finally:
        cursor.close()
        conexao.close()


def consulta_placa():
    placa = input("\nDigite a placa do veículo: ")
    conexao = conecta()

    try:
        cursor = conexao.cursor()

        sql = """
        SELECT placa, marca, modelo, ano, cor, km_atual, sinistro
        FROM carros
        WHERE placa = %s
        """
        cursor.execute(sql, (placa,))
        resultado = cursor.fetchone()

        if resultado:

            print("\n===== VEÍCULO ENCONTRADO =====\n")

            print(f"Placa: {resultado[0]}")
            print(f"Marca: {resultado[1]}")
            print(f"Modelo: {resultado[2]}")
            print(f"Ano: {resultado[3]}")
            print(f"Cor: {resultado[4]}")
            print(f"KM atual: {resultado[5]}")
            print(f"Sinistro: {'Sim' if resultado[6] else 'Não'}")

            print("\n==============================\n")    

        else:
            print("\nVeículo não encontrado!")

    except Exception as e:
        print(f"\nErro na consulta: {e}")

    finally:
        cursor.close()
        conexao.close()      


def consulta_email():
    email = input("\nDigite o e-mail do usuário: ")
    conexao = conecta()

    try:
        cursor = conexao.cursor()

        sql = """
        SELECT id, nome, email, telefone
        FROM usuarios
        WHERE email = %s
        """
        cursor.execute(sql, (email,))
        resultado = cursor.fetchone()

        if resultado:

            print("\n===== USUÁRIO ENCONTRADO =====\n")

            print(f"ID: {resultado[0]}")
            print(f"Nome: {resultado[1]}")
            print(f"Email: {resultado[2]}")
            print(f"Telefone: {resultado[3]}")
            
            print("\n==============================\n")    
            return resultado[0]

        else:
            print("\nUsuário não encontrado!")

    except Exception as e:
        print(f"\nErro na consulta: {e}")

    finally:
        cursor.close()
        conexao.close()     


def cadastro_tipo_manutencao():
    novo_tipo = TipoManutencao.coletar_dados()
    conexao = conecta()
    try:
        cursor = conexao.cursor()

        sql = """
        INSERT INTO tipo_manutencao (nome, descricao, intervalo_km, intervalo_meses)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (
            novo_tipo.nome,
            novo_tipo.descricao,
            novo_tipo.intervalo_km,
            novo_tipo.intervalo_meses
        ))

        conexao.commit()
        novo_tipo.id = cursor.lastrowid
        print("\n Tipo de manutenção cadastrado!")
        novo_tipo.exibir_dados()

    except Exception as e:
        conexao.rollback()
        print(f"\n Erro ao cadastrar tipo de manutenção: {e}")

    finally:
        cursor.close()
        conexao.close() 


def cadastro_novo_fornecedor():
    novo_fornecedor = Fornecedor.coletar_dados()
    conexao = conecta()
    try:
        cursor = conexao.cursor()

        sql = """
        INSERT INTO fornecedores (nome, telefone, especialidade)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (
            novo_fornecedor.nome,
            novo_fornecedor.telefone,
            novo_fornecedor.especialidade
        ))

        conexao.commit()
        novo_fornecedor.id = cursor.lastrowid
        print("\n Fornecedor cadastrado!")
        novo_fornecedor.exibir_dados()

    except Exception as e:
        conexao.rollback()
        print(f"\n Erro ao cadastrar fornecedor: {e}")

    finally:
        cursor.close()
        conexao.close()

def remover_usuario():
    print("Em desenvolvimento:)")

def remover_carro():
    conexao = conecta()
    placa = input("\nDigite a placa: ").strip()
    try:
        cursor = conexao.cursor()
        sql = """
        DELETE FROM carros
        WHERE placa = %s;"""

        cursor.execute(sql,(placa,))

        conexao.commit()
        print("\n Carro removido!")

    except Exception as e:
        conexao.rollback()
        print(f"\n Erro ao remover carro: {e}")
    finally:
        cursor.close()
        conexao.close()

def remover_tipo_manutencao():
    print("Em desenvolvimento:)")

def remover_fornecedor():
    print("Em desenvolvimento:)")