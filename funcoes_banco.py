from conexao import conecta
from classes.usuario import Usuario

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
