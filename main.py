from classes.carro import Carro


def main():

    carro1 = Carro(
        "ABC1234",
        "Toyota",
        "Corolla",
        2020,
        "Prata",
        50000
    )

    carro1.exibir_dados()

from classes.usuario import Usuario

usuario1 = Usuario(
    1,
    "Sabrina",
    "sabrina@gmail.com",
    "(51)99999-9999",
    "123456"
)

usuario1.exibir_dados()

print(usuario1)

main()

#teste da classe carro.py e usuario.py