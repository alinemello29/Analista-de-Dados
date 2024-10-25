![Screenshot 2024-10-23 14 26 30](https://github.com/user-attachments/assets/7183ce61-bcdf-4579-88ff-1a8d85dabbc6)

# Sistema de Gerenciamento de Funcionários

## 🎉 Descrição do Projeto

Bem-vindo ao nosso projeto de **Sistema de Gerenciamento de Funcionários**! Você foi contratado para desenvolver um sistema básico que permite à pequena empresa gerenciar suas informações de funcionários de forma eficiente. 

Este sistema é uma excelente oportunidade para praticar conceitos fundamentais em Python, como operadores, estruturas de controle, estruturas de dados e funções, enquanto constrói um aplicativo útil.

## 🚀 Funcionalidades do Sistema

O sistema oferece as seguintes funcionalidades:

1. **Adicionar Funcionário:**
   - Cadastro de novos funcionários, coletando informações como nome, cargo, salário, e-mail, entre outros.

2. **Atualizar Funcionário:**
   - Atualização das informações de um funcionário existente com base em um identificador único, como nome ou número de identificação.

3. **Listar Funcionários:**
   - Exibição de todos os funcionários cadastrados no sistema.

4. **Remover Funcionário:**
   - Possibilidade de remover um funcionário do sistema.

## 🛠️ Requisitos

Para implementar o sistema, utilizamos a função `input()` para coletar dados dos usuários. As informações coletadas incluem:

- Nome
- Cidade e Estado de residência
- Idade
- Escolaridade
- Cargo
- Salário

### Observações Importantes:

- **Identificação Única:** É fundamental implementar um sistema de identificação único para cada funcionário.
- **Validação de Entradas:** Garantir que as entradas do usuário sejam validadas para evitar erros durante as operações.
- **Documentação:** O código deve ser devidamente comentado para facilitar a compreensão.

## 📜 Exemplo de Implementação

Aqui está um esboço básico de como o sistema pode ser estruturado:

```python
# Lista para armazenar funcionários
funcionarios = []

# Função para adicionar funcionário
def adicionar_funcionario():
    nome = input("Informe o nome do funcionário: ")
    cargo = input("Informe o cargo: ")
    salario = float(input("Informe o salário: "))
    # Outros dados...
    funcionario = {
        'nome': nome,
        'cargo': cargo,
        'salario': salario,
        # Adicionar outros campos
    }
    funcionarios.append(funcionario)
    print(f"Funcionário {nome} adicionado com sucesso!")

# Função para listar funcionários
def listar_funcionarios():
    for funcionario in funcionarios:
        print(funcionario)

# Implementar funções de atualizar e remover

# Menu principal
while True:
    print("1 - Adicionar Funcionário")
    print("2 - Listar Funcionários")
    # Outras opções...
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        adicionar_funcionario()
    elif escolha == '2':
        listar_funcionarios()
    # Outras condições...