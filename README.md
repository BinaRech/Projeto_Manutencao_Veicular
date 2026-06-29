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

# 🚗 DriveAlert System

Sistema de Gerenciamento de Manutenção Veicular desenvolvido em **Python** com **Programação Orientada a Objetos (POO)**, **MySQL** e integração com a **API do Telegram**.

O objetivo do sistema é permitir o cadastro de usuários, veículos e manutenções, além de enviar notificações automáticas quando uma revisão estiver próxima da data programada.

---

# 📌 Objetivo

O DriveAlert System foi desenvolvido para auxiliar proprietários de veículos no controle das manutenções preventivas e corretivas.

Muitos motoristas esquecem datas importantes de revisão, troca de óleo, pneus, filtros e outras manutenções essenciais. O sistema resolve esse problema armazenando essas informações em banco de dados e enviando lembretes automáticos pelo Telegram.

---

# 🚀 Funcionalidades

01. Usuários

* Cadastro de usuários
* Consulta por e-mail
* Cadastro do Telegram ID
* Associação entre usuário e veículo

---

02. Veículos

* Cadastro de veículos
* Consulta por placa
* Controle de quilometragem
* Registro de sinistro

---

03. Tipos de manutenção

* Cadastro de tipos de manutenção
* Descrição
* Intervalo em quilômetros
* Intervalo em meses

---

04. Fornecedores

* Cadastro de fornecedores
* Especialidade
* Telefone

---

05. Manutenções

* Cadastro de manutenção
* Associação ao veículo
* Data da revisão
* Quilometragem
* Observações

---

06. Alertas automáticos

O sistema verifica diariamente as manutenções cadastradas e envia notificações quando faltam:

* 30 dias
* 15 dias
* 7 dias
* 1 dia
* No próprio dia da revisão

As notificações são enviadas automaticamente através do Telegram.

---

# 🏗️ Arquitetura

O projeto foi desenvolvido utilizando Programação Orientada a Objetos.

Principais classes:

* Usuario
* Carro
* TipoManutencao
* Fornecedor
* Documento
* Manutencao
* Sistema

Cada classe possui responsabilidades específicas, mantendo o código organizado e modular.

---

# 🗂️ Estrutura do projeto

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

# 💻 Tecnologias utilizadas

* Python 3
* MySQL
* MySQL Connector
* Requests
* Telegram Bot API
* Railway (Banco de Dados)

---

# 🗄️ Banco de Dados

Principais tabelas:

* usuarios
* carros
* manutencao
* tipo_manutencao
* fornecedores

Relacionamentos:

* Um usuário pode possuir vários veículos.
* Um veículo pode possuir várias manutenções.
* Cada manutenção pertence a um tipo de manutenção.

---

# 📲 Integração com Telegram

O sistema utiliza a API oficial do Telegram para envio de notificações automáticas.

Fluxo:

1. Usuário inicia conversa com o bot.
2. Telegram ID é cadastrado no sistema.
3. O sistema verifica as revisões pendentes.
4. A notificação é enviada automaticamente ao proprietário.

---

# ▶️ Como executar

## Instalar dependências

```bash
pip install mysql-connector-python
pip install requests
```

---

## Executar

```bash
python main.py
```

---

# 📋 Menu principal

```text
1 - Cadastros
2 - Consultas
3 - Remoções
4 - Verificar alertas de manutenção
0 - Sair
```

---

# 📖 Fluxo de utilização

1. Cadastrar usuário.
2. Informar Telegram ID.
3. Cadastrar veículo.
4. Cadastrar tipo de manutenção.
5. Cadastrar fornecedor.
6. Registrar manutenção.
7. Executar a verificação de alertas.
8. Receber a notificação pelo Telegram.

---

📲 Obtendo o Telegram ID

Para que o sistema consiga enviar notificações ao usuário, é necessário cadastrar o Telegram ID de cada proprietário.

Passo 1

Abra o bot do projeto no Telegram:

@DriveAlertSystemBot

Clique em Start ou envie:

/start

Passo 2

No navegador, acesse:

[https://api.telegram.org/botSEU_TOKEN/getUpdates] -> (https://api.telegram.org/bot8821945772:AAHv8FejJiq-ElB4UtoQcCAxQEUS9fQHnpg/getUpdates)

Substitua SEU_TOKEN pelo token do bot criado no BotFather.

Passo 3

No retorno da API, procure pela informação:

{
    "chat": {
        "id": 8373766961,
        "first_name": "Eduardo"
    }
}

O valor do campo:

id

é o Telegram ID do usuário.

No exemplo acima:

Telegram ID = 8373766961

Passo 4

Durante o cadastro do usuário no sistema, informe esse número quando solicitado:

===== CADASTRO DE USUÁRIO =====

Nome: Eduardo
Email: eduardo@email.com
Telefone: 51999999999
Telegram ID: 8373766961
Senha: ********

Após esse cadastro, o sistema enviará automaticamente as notificações para o Telegram do usuário sempre que uma manutenção estiver próxima da data programada.

---

# 👥 Equipe

Projeto desenvolvido para a disciplina de Fábrica de Software.

Integrantes:

* Sabrina
* Eduardo
* Rafael

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
