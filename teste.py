# ================================================ #
#  Arquivo de Testes                               #
#  Utilizado para testar as classes do sistema     #
#  durante o desenvolvimento, sem usar o banco     #
#  de dados ou o menu principal.                   #
# ================================================ #

from classes.usuario import Usuario
from classes.carro import Carro
from classes.tipo_manutencao import TipoManutencao
from classes.manutencao import Manutencao
from classes.fornecedor import Fornecedor
from classes.documento import Documento

from datetime import datetime


# TESTE USUÁRIO
usuario = Usuario(
    1,
    "Sabrina",
    "sabrina@gmail.com",
    "(51)99999-9999",
    "123456"
)

usuario.exibir_dados()


# TESTE CARRO
carro = Carro(
    "ABC1234",
    "Toyota",
    "Corolla",
    2020,
    "Prata",
    50000
)

carro.exibir_dados()


# TESTE FORNECEDOR
fornecedor = Fornecedor(
    1,
    "Oficina do João",
    "(51)99999-1111",
    "Troca de óleo"
)

fornecedor.exibir_dados()


# TESTE TIPO MANUTENÇÃO
tipo = TipoManutencao(
    1,
    "Troca de Óleo",
    "Substituição do óleo do motor",
    6
)

tipo.exibir_dados()


# TESTE MANUTENÇÃO
manutencao = Manutencao(
    1,
    carro.placa,
    tipo,
    datetime.now(),
    250.00,
    fornecedor.nome,
    "Troca realizada sem problemas."
)

manutencao.exibir_dados()


# TESTE DOCUMENTO
documento = Documento(
    1,
    manutencao.id_manutencao,
    "nota_fiscal.pdf",
    "documentos/nota_fiscal.pdf"
)

documento.exibir_dados()


# TESTE VÍNCULO CARRO x MANUTENÇÃO
carro.adicionar_manutencao(manutencao)

print("Quantidade de manutenções cadastradas:")
print(len(carro.manutencoes))


# TESTE VÍNCULO USUÁRIO x CARRO
usuario.adicionar_veiculo(carro)

print("\nVeículos cadastrados para o usuário:")
print(len(usuario.veiculos))