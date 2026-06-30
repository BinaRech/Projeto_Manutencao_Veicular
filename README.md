# Projeto_Manutencao_Veicular
Sistema de gerenciamento de manutenção veicular desenvolvido em Python Orientado a Objetos para a disciplina de Fábrica de Software.
bibliotecas:
    pip install mysql-connector-python
prompt:
    me liste os comando da biblioteca de python mysql.connector e os explique
connect() → conecta no banco
cursor() → prepara execução
execute() → roda SQL
fetch*() → pega dados
commit() → salva mudanças
close() → encerra tudo

------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚗 DriveAlert System

Sistema de Gerenciamento de Manutenção Veicular desenvolvido em **Python** com **Programação Orientada a Objetos (POO)**, **MySQL** e integração com a **API do Telegram**.

O objetivo do sistema é permitir o cadastro de usuários, veículos e manutenções, além de enviar notificações automáticas quando uma revisão estiver próxima da data programada.

---

## 📌 Objetivo

O DriveAlert System foi desenvolvido para auxiliar proprietários de veículos no controle das manutenções preventivas e corretivas.

O sistema permite cadastrar usuários, veículos, fornecedores, tipos de manutenção e registrar o histórico de serviços realizados.

Com base nas informações cadastradas, o sistema calcula automaticamente a próxima revisão considerando tanto o intervalo de tempo quanto o intervalo de quilometragem definido para cada tipo de manutenção, enviando notificações automáticas pelo Telegram quando uma revisão estiver próxima ou quando a quilometragem recomendada estiver prestes a ser atingida.

---

## 🚀 Funcionalidades

## 01. Usuários

* Cadastro de usuários
* Consulta por e-mail
* Cadastro do Telegram ID
* Associação entre usuário e veículo
* Remoção de usuários

---

## 02. Veículos

* Cadastro de veículos
* Consulta por placa
* Atualização da quilometragem
* Controle de quilometragem
* Registro de sinistro
* Remoção de veículos

---

## 03. Tipos de manutenção

* Cadastro de tipos de manutenção
* Descrição
* Intervalo em quilômetros
* Intervalo em meses
* Remoção de tipos de manutenção

---

## 04. Fornecedores

* Cadastro de fornecedores
* Especialidade
* Telefone
* Remoção de fornecedores

---

## 05. Manutenções

* Cadastro de manutenção
* Associação ao veículo
* Registro da data da última manutenção
* Registro da quilometragem da manutenção
* Observações
* Consulta ao histórico completo de manutenções por placa

---

## 06. Alertas automáticos

O sistema calcula automaticamente a próxima revisão considerando:

* Intervalo em meses.
* Intervalo em quilômetros.

Os alertas são enviados quando:

* faltam 30 dias;
* faltam 15 dias;
* faltam 7 dias;
* falta 1 dia;

As notificações são enviadas automaticamente através da API do Telegram.

---

## 🏗️ Arquitetura

O projeto foi desenvolvido utilizando Programação Orientada a Objetos.

Principais classes:

* Usuario
* Carro
* TipoManutencao
* Fornecedor
* Documento
* Manutencao
* Sistema

---

## 🗂️ Estrutura do projeto

```text
Projeto_Manutencao_Veicular/

│
├── classes/
│   ├── usuario.py
│   ├── carro.py
│   ├── fornecedor.py
│   ├── documento.py
│   ├── manutencao.py
│   ├── tipo_manutencao.py
│   └── sistema.py
│
├── conexao.py
├── funcoes_banco.py
├── main.py
│
└── README.md
```

---

## 💻 Tecnologias utilizadas

* Python 3
* MySQL
* MySQL Connector
* Requests
* Telegram Bot API
* Railway (Banco de Dados)

---

## 🗄️ Banco de Dados

Principais tabelas:

* usuarios
* carros
* manutencao
* tipo_manutencao
* fornecedores

Relacionamentos:

* Um usuário pode possuir vários veículos.
* Um veículo pertence a um único usuário.
* Um veículo pode possuir várias manutenções.
* Cada manutenção pertence a um tipo de manutenção.
* Cada tipo de manutenção possui um intervalo em quilômetros e/ou em meses.

---

## 📲 Integração com Telegram

O sistema utiliza a API oficial do Telegram para envio automático de notificações aos proprietários dos veículos.

Fluxo:

1. O usuário inicia uma conversa com o bot do projeto.
2. O Telegram ID é obtido através da API do Telegram.
3. O Telegram ID é informado durante o cadastro do usuário.
4. O sistema calcula automaticamente a próxima revisão utilizando a data da última manutenção e os intervalos cadastrados.
5. Quando uma revisão estiver próxima por tempo ou por quilometragem, uma mensagem é enviada automaticamente ao proprietário do veículo.

---

## ▶️ Como executar

## Instalar as dependências

```bash
pip install mysql-connector-python
pip install requests
```

---

## Executar o sistema

```bash
python main.py
```

---

## Observações

O projeto já está configurado para utilizar o banco de dados remoto hospedado no Railway, cujas informações de conexão estão definidas no arquivo `conexao.py`.

Para utilizar as notificações automáticas via Telegram, é necessário que cada usuário informe seu **Telegram ID** durante o cadastro.

## 📋 Menu principal

```text
1 - Cadastros
2 - Consultas
3 - Remoções
4 - Verificar alertas de manutenção
5 - Atualizar KM do veículo
0 - Sair
```

---

## 📖 Fluxo de utilização

1. Cadastrar usuário.
2. Informar Telegram ID.
3. Cadastrar veículo.
4. Cadastrar tipo de manutenção.
5. Cadastrar fornecedor.
6. Registrar uma manutenção realizada.
7. Atualizar a quilometragem do veículo sempre que necessário.
8. Consultar o histórico de manutenções por placa.
9. Executar a verificação de alertas.
10. Receber automaticamente a notificação pelo Telegram.

---

## 📲 Obtendo o Telegram ID

Para que o sistema consiga enviar notificações ao usuário, é necessário cadastrar o Telegram ID de cada proprietário.

## Passo 1

Abra o bot do projeto no Telegram: @DriveAlertSystemBot
Clique em Start ou envie: /start

## Passo 2

No navegador, acesse:

[https://api.telegram.org/botSEU_TOKEN/getUpdates] -> (https://api.telegram.org/bot8821945772:AAHv8FejJiq-ElB4UtoQcCAxQEUS9fQHnpg/getUpdates)
Substitua SEU_TOKEN pelo token do bot criado no BotFather.

## Passo 3

No retorno da API, procure pela informação:

{
    "chat": {
        "id": 8373766961,
        "first_name": "Eduardo"
    }
}

O valor do campo id é o Telegram ID do usuário.
No exemplo acima:
Telegram ID = 8373766961

## Passo 4

Após esse cadastro, o sistema calculará automaticamente a próxima revisão com base na última manutenção registrada, considerando os intervalos de tempo e de quilometragem definidos para cada tipo de manutenção. Quando uma revisão estiver próxima, uma notificação será enviada automaticamente ao Telegram do proprietário.

===== CADASTRO DE USUÁRIO =====

Nome: Eduardo
Email: eduardo@email.com
Telefone: 51999999999
Telegram ID: 8373766961
Senha: ********

Após esse cadastro, o sistema enviará automaticamente as notificações para o Telegram do usuário sempre que uma manutenção estiver próxima da data programada.

---

## Declaração de utilização de Inteligência Artificial (Sabrina Rech)

Durante o desenvolvimento deste projeto foi utilizada Inteligência Artificial (ChatGPT - OpenAI) como ferramenta de apoio à programação.

A utilização ocorreu principalmente para:

- esclarecimento de dúvidas sobre Python;
- revisão de lógica de programação;
- auxílio na escrita de consultas SQL;
- identificação e correção de erros;
- documentação do projeto (README);
- elaboração de casos de teste.

Todo o código gerado foi analisado, adaptado, integrado e testado antes de sua utilização no projeto.

A Inteligência Artificial foi utilizada apenas como ferramenta de apoio ao desenvolvimento, não substituindo a compreensão, implementação, validação e integração realizada por mim.

## Prompt 1 - Integração com Telegram

Prompt:
Auxilie na integração do sistema com a API do Telegram para envio automático de notificações.

Resposta (resumo):
Foi sugerida a utilização da Telegram Bot API para envio de mensagens automáticas aos usuários cadastrados.

## Prompt 2 - Cálculo automático das revisões

Prompt:
Auxilie na implementação da lógica para cálculo automático da próxima revisão utilizando intervalo de tempo e quilometragem.

Resposta (resumo):
Foi proposta uma lógica que calcula automaticamente a próxima revisão considerando a data da última manutenção, o intervalo em meses e o intervalo em quilômetros definidos para cada tipo de manutenção.

## Prompt 3 - Atualização da quilometragem

Prompt:
Auxilie na implementação da atualização da quilometragem do veículo e sua integração com o cálculo das revisões.

Resposta (resumo):
Foi sugerida uma função responsável por atualizar a quilometragem do veículo e utilizá-la no cálculo dos alertas automáticos.

--> Cópia
```text
        # atualiza a quilometragem
        sql_update = """
        UPDATE carros
        SET km_atual = %s
        WHERE placa = %s
        """
```

## Prompt 4 - Consulta ao histórico

Prompt:
Auxilie na implementação da consulta do histórico de manutenções por placa.

Resposta (resumo):
Foi sugerida uma consulta SQL responsável por recuperar todas as manutenções realizadas para um determinado veículo.

--> Cópia
```text
        sql = """
        SELECT
            m.id,
            m.placa,
            t.nome,
            m.tipo_manutencao,
            m.data_revisao,
            m.km_atual,
            m.observacao
        FROM manutencao m
        INNER JOIN tipo_manutencao t
        ON m.tipo_revisao_id = t.id
        WHERE m.placa = %s
        ORDER BY m.data_revisao DESC
        """
```

## Prompt 5 - Revisão de lógica

Prompt:
Revise a lógica do sistema e identifique possíveis inconsistências ou erros de funcionamento.

Resposta (resumo):
Foram identificadas inconsistências relacionadas ao cálculo da próxima revisão, utilização da data da manutenção e geração de alertas duplicados, posteriormente corrigidas durante o desenvolvimento.

## Prompt 6 — Documentação

Prompt:
Auxilie na elaboração do README do projeto.

Resposta (resumo):
Foi produzida uma estrutura inicial da documentação contendo descrição do projeto, funcionalidades, arquitetura, tecnologias utilizadas e instruções de execução.

## Prompt 7 - Validação das funcionalidade do sistema

Prompt:
vamos usar o cadastro da Sabrina para testar todas funções possiveis e valida-las

Resposta:
Foi o passo a passo pra testar todas as funções do sistema de forma completa(esse não tem pdf).

## Prompt 8 - Casos de Teste

Prompt:
faça o caso de teste do eduardo, mas com as coisas valendo e agora checando apenas a mensagem por data(sem a km ter atingido o limite) ai cadastra o Rafael(e ele sim vc faz verificando os erros), faz exatamente igual vc fez com a Sabrina(so lembra que os 4 tipos de manutenção ja estão cadstradas) e me manda em pdf.

Resposta:
```text
Caso de Teste 03 - Eduardo
Caso de Teste 04 - Rafael
```
