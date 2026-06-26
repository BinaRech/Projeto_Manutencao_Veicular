class Fornecedor:
    def __init__(self, id, nome, telefone, especialidade):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.especialidade = especialidade

    def exibir_dados(self):

        print("\n===== FORNECEDOR =====\n")

        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Especialidade: {self.especialidade}")

        print("\n======================\n")

    def __str__(self):
        return self.nome


def cadastrar_fornecedor(fornecedores, id, nome, telefone, especialidade):
    """Cria um novo fornecedor e adiciona à lista de fornecedores."""
    if buscar_fornecedor_por_id(fornecedores, id) is not None:
        raise ValueError(f"Já existe um fornecedor com ID {id}.")

    fornecedor = Fornecedor(id, nome, telefone, especialidade)
    fornecedores.append(fornecedor)
    return fornecedor


def buscar_fornecedor_por_id(fornecedores, id):
    """Retorna o fornecedor com o ID informado, ou None se não existir."""
    for fornecedor in fornecedores:
        if fornecedor.id == id:
            return fornecedor
    return None


def editar_fornecedor(fornecedores, id, nome=None, telefone=None, especialidade=None):
    """Edita os dados de um fornecedor existente."""
    fornecedor = buscar_fornecedor_por_id(fornecedores, id)
    if fornecedor is None:
        raise ValueError(f"Fornecedor com ID {id} não encontrado.")

    if nome is not None:
        fornecedor.nome = nome
    if telefone is not None:
        fornecedor.telefone = telefone
    if especialidade is not None:
        fornecedor.especialidade = especialidade

    return fornecedor


def excluir_fornecedor(fornecedores, id):
    """Remove o fornecedor com o ID informado da lista."""
    fornecedor = buscar_fornecedor_por_id(fornecedores, id)
    if fornecedor is None:
        raise ValueError(f"Fornecedor com ID {id} não encontrado.")

    fornecedores.remove(fornecedor)
    return fornecedor
