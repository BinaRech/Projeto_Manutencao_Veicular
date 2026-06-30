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
        INSERT INTO usuarios (nome, email, telefone, senha, telegram_id)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            novo_usuario.nome,
            novo_usuario.email,
            novo_usuario.telefone,
            novo_usuario.senha,
            novo_usuario.telegram_id
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
        SELECT id, nome, email, telefone, telegram_id
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
            print(f"Telegram ID: {resultado[4]}")
            
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


def remover_carro():
    
    placa = input("\nDigite a placa: ").strip()
    conexao = conecta()

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


def remover_usuario():
    usuario_id = consulta_email()

    if usuario_id is None:
        print("\n Usuário não encontrado.")
        return

    conexao = conecta()
    try:
        cursor = conexao.cursor()

        # remove todos os carros do usuario primeiro
        sql_carros = """
        DELETE FROM carros
        WHERE usuario_id = %s
        """
        cursor.execute(sql_carros, (usuario_id,))
        carros_removidos = cursor.rowcount  # conta as linhas realizadas no sql para saber quantos removeu

        # remove o usuario
        sql_usuario = """
        DELETE FROM usuarios
        WHERE id = %s
        """
        cursor.execute(sql_usuario, (usuario_id,))

        conexao.commit()
        print(f"\n Usuário removido com sucesso!")
        print(f" Veículos removidos junto: {carros_removidos}")

    except Exception as e:
        conexao.rollback()
        print(f"\n Erro ao remover usuário: {e}")

    finally:
        cursor.close()
        conexao.close()


def remover_tipo_manutencao():
    
    id_manutecao = int(input("\nDigite o id do tipo de manuteção: "))
    conexao = conecta()

    try:
        cursor = conexao.cursor()
        sql = """
        DELETE FROM tipo_manutencao
        WHERE id = %s;"""

        cursor.execute(sql,(id_manutecao,))

        conexao.commit()
        print("\n Tipo de manutenção removida!")

    except Exception as e:
        conexao.rollback()
        print(f"\n Erro ao remover manutenção: {e}")

    finally:
        cursor.close()
        conexao.close()


def remover_fornecedor():

    id_fornecedor = int(input("\nDigite o id do fornecedor: "))
    conexao = conecta()

    try:
        cursor = conexao.cursor()
        sql = """
        DELETE FROM fornecedores
        WHERE id = %s;"""

        cursor.execute(sql,(id_fornecedor,))

        conexao.commit()
        print("\n fornecedor removido!")

    except Exception as e:
        conexao.rollback()
        print(f"\n Erro ao remover fornecedor: {e}")

    finally:
        cursor.close()
        conexao.close()


def buscar_telegram_id(email):

    conexao = conecta()
    
    try:
        cursor = conexao.cursor()

        sql = """
        SELECT telegram_id
        FROM usuarios
        WHERE email = %s
        """

        cursor.execute(sql,(email,))
        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]
        else:
            print("Usuário não encontrado!")
            return None

    except Exception as e:
        print(f"Erro ao buscar Telegram ID: {e}")

    finally:
        cursor.close()
        conexao.close()


def cadastro_manutencao():

    print("\n===== CADASTRO DE MANUTENÇÃO =====")

    listar_tipos_manutencao()

    placa = input("Placa do veículo: ").strip().upper()
    tipo_revisao_id = int(input("ID do tipo de manutenção: "))
    tipo_manutencao = input("Tipo de manutenção (Preventiva/Corretiva): ").strip().capitalize()
    data_revisao = input("Data da revisão (AAAA-MM-DD): ")
    km_atual = int(input("KM atual: "))
    observacao = input("Observação: ")

    conexao = conecta()
    
    try:
        cursor = conexao.cursor()

        sql = """
        INSERT INTO manutencao
        (placa, tipo_revisao_id, tipo_manutencao, data_revisao, km_atual, observacao)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            placa,
            tipo_revisao_id,
            tipo_manutencao,
            data_revisao,
            km_atual,
            observacao
        ))

        conexao.commit()

        print("Manutenção cadastrada com sucesso!")
     

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao cadastrar manutencao: {e}")

    finally:
        cursor.close()
        conexao.close()

def buscar_telegram_por_placa(placa):

    conexao = conecta()

    try:
        cursor = conexao.cursor()

        sql = """
        SELECT usuarios.telegram_id
        FROM usuarios
        INNER JOIN carros
        ON usuarios.id = carros.usuario_id
        WHERE carros.placa = %s
        """

        cursor.execute(sql, (placa,))
        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]

        return None

    except Exception as e:
        print(f"Erro ao buscar Telegram pela placa: {e}")
        return None

    finally:
        cursor.close()
        conexao.close()


def listar_tipos_manutencao():

    conexao = conecta()

    try:
        cursor = conexao.cursor()

        sql = """
        SELECT id, nome, descricao, intervalo_km, intervalo_meses
        FROM tipo_manutencao
        ORDER BY id
        """

        cursor.execute(sql)
        tipos = cursor.fetchall()

        if tipos:
            print("\n===== TIPOS DE MANUTENÇÃO CADASTRADOS =====\n")

            print(f"{'ID':<5} {'Nome':<25} {'Intervalo KM':<15} {'Meses':<10}")

            for tipo in tipos:
                print(f"{tipo[0]:<5} {tipo[1]:<25} {str(tipo[3]):<15} {str(tipo[4]):<10}")

            print("\n===========================================\n")
        else:
            print("\nNenhum tipo de manutenção cadastrado.")

    except Exception as e:
        print(f"Erro ao listar tipos de manutenção: {e}")

    finally:
        cursor.close()
        conexao.close()