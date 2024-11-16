# -*- coding: utf-8 -*-
"""Alan

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14ONl9KllaPXW6ZTwRVTnMcIoF7MlReZd
"""

# Declarando o dicionário globalmente para armazenar funcionários
funcionarios = {}
proximo_id = 1  # Variável global para gerar um ID único para cada funcionário

def adicionar_funcionario():
    global proximo_id, funcionarios
    print("\nCadastro de Novo Funcionário:")
    nome = input("Nome: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    idade = input("Idade: ")
    escolaridade = input("Escolaridade: ")
    cargo = input("Cargo: ")

    while True:
        try:
            salario = float(input("Salário: "))
            break
        except ValueError:
            print("Por favor, insira um valor numérico válido para o salário.")

    email = input("E-mail: ")
    funcionarios[proximo_id] = {
        'nome': nome, 'cidade': cidade, 'estado': estado, 'idade': idade,
        'escolaridade': escolaridade, 'cargo': cargo, 'salario': salario, 'email': email
    }
    print(f"Funcionário {nome} adicionado com ID: {proximo_id}")
    proximo_id += 1

def atualizar_funcionario():
    global funcionarios
    try:
        id_funcionario = int(input("\nDigite o ID do funcionário que deseja atualizar: "))
        if id_funcionario in funcionarios:
            print("\nAtualizando informações do funcionário:")
            nome = input("Novo Nome (deixe vazio para manter o atual): ") or funcionarios[id_funcionario]['nome']
            cidade = input("Nova Cidade (deixe vazio para manter a atual): ") or funcionarios[id_funcionario]['cidade']
            estado = input("Novo Estado (deixe vazio para manter o atual): ") or funcionarios[id_funcionario]['estado']
            idade = input("Nova Idade (deixe vazio para manter a atual): ") or funcionarios[id_funcionario]['idade']
            escolaridade = input("Nova Escolaridade (deixe vazio para manter a atual): ") or funcionarios[id_funcionario]['escolaridade']
            cargo = input("Novo Cargo (deixe vazio para manter o atual): ") or funcionarios[id_funcionario]['cargo']

            while True:
                salario_input = input("Novo Salário (deixe vazio para manter o atual): ")
                if not salario_input:
                    salario = funcionarios[id_funcionario]['salario']
                    break
                try:
                    salario = float(salario_input)
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para o salário.")

            email = input("Novo E-mail (deixe vazio para manter o atual): ") or funcionarios[id_funcionario]['email']
            funcionarios[id_funcionario] = {
                'nome': nome, 'cidade': cidade, 'estado': estado, 'idade': idade,
                'escolaridade': escolaridade, 'cargo': cargo, 'salario': salario, 'email': email
            }
            print(f"Informações do funcionário ID {id_funcionario} atualizadas com sucesso.")
        else:
            print("Funcionário com este ID não encontrado.")
    except ValueError:
        print("Por favor, insira um ID numérico válido.")

def exibir_funcionario():
    global funcionarios
    try:
        id_funcionario = int(input("\nDigite o ID do funcionário que deseja visualizar: "))
        if id_funcionario in funcionarios:
            print(f"\nInformações do Funcionário ID {id_funcionario}:")
            for chave, valor in funcionarios[id_funcionario].items():
                print(f"{chave.capitalize()}: {valor}")
        else:
            print("Funcionário com este ID não encontrado.")
    except ValueError:
        print("Por favor, insira um ID numérico válido.")

def listar_funcionarios():
    global funcionarios
    if funcionarios:
        print("\nLista de Funcionários Cadastrados:")
        for id_funcionario, dados in funcionarios.items():
            print(f"ID: {id_funcionario} | Nome: {dados['nome']} | Cargo: {dados['cargo']}")
    else:
        print("\nNenhum funcionário cadastrado no momento.")

def remover_funcionario():
    global funcionarios
    try:
        id_funcionario = int(input("\nDigite o ID do funcionário que deseja remover: "))
        if id_funcionario in funcionarios:
            confirmacao = input(f"Tem certeza de que deseja remover o funcionário {funcionarios[id_funcionario]['nome']}? (S/N): ")
            if confirmacao.lower() == 's':
                del funcionarios[id_funcionario]
                print(f"Funcionário com ID {id_funcionario} removido com sucesso.")
            else:
                print("Remoção cancelada.")
        else:
            print("Funcionário com este ID não encontrado.")
    except ValueError:
        print("Por favor, insira um ID numérico válido.")

# Menu de opções
def menu():
    while True:
        print("\n--- Sistema de Gestão de Funcionários ---")
        print("1. Adicionar novo funcionário")
        print("2. Atualizar informações de funcionário")
        print("3. Exibir informações de um funcionário")
        print("4. Listar todos os funcionários")
        print("5. Remover um funcionário")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_funcionario()
        elif opcao == '2':
            atualizar_funcionario()
        elif opcao == '3':
            exibir_funcionario()
        elif opcao == '4':
            listar_funcionarios()
        elif opcao == '5':
            remover_funcionario()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")