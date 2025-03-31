# Banking App
This Python program is a simple banking application that allows users to manage accounts, track transactions, and view financial summaries. The application provides a command-line interface for interacting with banking operations.

**Technologies Used**

    SQLModel: An ORM (Object-Relational Mapping) library that combines SQLAlchemy with Pydantic, used for database operations and data validation

    SQLite: A lightweight disk-based database used for persistent storage

    Matplotlib: A plotting library used for generating visualizations of account data

    Python's Enum: Used for creating enumerated constants for banks, account statuses, and transaction types

**Data Model**

    Conta (Account): Represents bank accounts with fields for ID, balance (valor), bank (banco), and status (ativo/inativo)

    Historico (History): Records financial transactions with fields for ID, account reference, transaction type (entrada/saida), amount (valor), and date

# Aplicativo Bancário

Este programa em Python é um aplicativo bancário simples que permite aos usuários gerenciar contas, acompanhar transações e visualizar resumos financeiros. A aplicação fornece uma interface de linha de comando para interagir com operações bancárias.

**Tecnologias Utilizadas**

    SQLModel: Uma biblioteca ORM (Mapeamento Objeto-Relacional) que combina SQLAlchemy com Pydantic, utilizada para operações de banco de dados e validação de dados.

    SQLite: Um banco de dados leve baseado em disco usado para armazenamento persistente.

    Matplotlib: Uma biblioteca de plotagem usada para gerar visualizações de dados das contas.

    Enum do Python: Utilizado para criar constantes enumeradas para bancos, status de contas e tipos de transação.

**Modelo de Dados**

    Conta (Account): Representa contas bancárias com campos para ID, saldo (valor), banco e status (ativo/inativo).

    Histórico (History): Registra transações financeiras com campos para ID, referência da conta, tipo de transação (entrada/saída), valor e data.