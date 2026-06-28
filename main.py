from funcoes_banco import (
    cadastro_usuario,
    cadastro_veiculo,
    consulta_placa,
    consulta_email,
    cadastro_tipo_manutencao,
    cadastro_novo_fornecedor,
    remover_usuario,
    remover_carro,
    remover_tipo_manutencao,
    remover_fornecedor,
)

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

tipo_remocao = {
    "1": remover_usuario,
    "2": remover_carro,
    "3": remover_tipo_manutencao,
    "4": remover_fornecedor,
}
def main():
 
    while True:
        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Cadastros")
        print("2 - Consultas")
        print("3 - Remoções")
        print("0 - Sair")
 
        opcao = input("Escolha: ").strip()
 
        if opcao == "0":
            print("\nEncerrando sistema...\n")
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

        elif opcao == "3":
            print("\n========== MENU REMOÇÕES ==========")
            print("1 - Remover Usuário(Remove os carros vinculados)")
            print("2 - Remover Carro")
            print("3 - Remover Tipo de Manutenção")
            print("4 - Remover Fornecedor")
            print("0 - Retornar")

            tipo = input("Escolha: ").strip()

            if tipo == "0":
                continue
            elif tipo in tipo_remocao:
                tipo_remocao[tipo]()
            else:
                print("Opção inválida.")
        
 
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

