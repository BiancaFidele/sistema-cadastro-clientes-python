#🔴 Nível 3 — Alto (case de portfólio)

#Título: Sistema de Cadastro de Clientes com Classe

#Contexto: Uma pequena empresa de serviços quer um sistema simples de terminal para cadastrar clientes, evitando duplicidade e 
#permitindo consultar quem já está cadastrado.

#Enunciado: Usando Programação Orientada a Objetos, crie uma classe Cliente com os atributos que você considerar relevantes (nome, telefone, cidade, etc). 
#Depois, crie um sistema com menu (while) que permita: cadastrar um novo cliente (impedindo cadastro duplicado pelo nome), 
#listar todos os clientes cadastrados, buscar um cliente pelo nome, e sair do sistema.

#Requisitos:

#Uma classe Cliente com __init__ e ao menos um método (ex: exibir informações)
#Uma estrutura (lista) para armazenar múltiplos objetos Cliente
#Lógica para verificar duplicidade antes de cadastrar
#Função de busca que percorra a lista de clientes
#Menu funcional em loop

#Resultado esperado: O sistema deve gerenciar múltiplos clientes na mesma execução, sem permitir nomes duplicados, e permitir buscar um cliente específico 
#sem precisar listar todos.

#Conhecimentos praticados: POO (classes, atributos, métodos), listas de objetos, funções, condicionais, while, f-strings.

#Entregáveis: código completo + pelo menos 3 testes mostrando: cadastro bem-sucedido, tentativa de duplicidade, e busca de um cliente existente.

print("Sistema de Cadastro")
print("Digite os dados dos clientes")


class Cliente:

    def __init__(self, nome, idade, telefone, cpf, cep, cidade, endereco, estado):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.cep = cep
        self.cidade = cidade
        self.endereco = endereco
        self.estado = estado

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Telefone: {self.telefone}")
        print(f"CPF: {self.cpf}")
        print(f"CEP: {self.cep}")
        print(f"Cidade: {self.cidade}")
        print(f"Endereço: {self.endereco}")
        print(f"Estado: {self.estado}")


def cadastrar_cliente(clientes):

    nome = input("\nNome: ")
    idade = int(input("Idade: "))
    telefone = input("Telefone: ")
    cpf = input("CPF: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    endereco = input("Endereço: ")
    estado = input("Estado: ")

    # verifica se o CPF já existe
    for cliente_cadastrado in clientes:
        if cliente_cadastrado.cpf == cpf:
            print("\nErro: já existe um cliente com esse CPF.\n")
            return

    novo_cliente = Cliente(
        nome,
        idade,
        telefone,
        cpf,
        cep,
        cidade,
        endereco,
        estado
    )

    clientes.append(novo_cliente)

    print("\nDados cadastrados com sucesso!\n")


def listar_clientes(clientes):

    if clientes:
        print("\nClientes Cadastrados:\n")

        for cliente in clientes:
            cliente.exibir_informacoes()
            print("--------------------")

    else:
        print("\nLista de clientes vazia.\n")

def buscar_nome(clientes):

    nome = input("\nDigite o nome do cliente que deseja buscar: ")

    for cliente_cadastrado in clientes:

        if cliente_cadastrado.nome.lower() == nome.lower():
            print("\nCliente encontrado:\n")
            cliente_cadastrado.exibir_informacoes()
            return

    print("\nCliente não encontrado.\n")


clientes = []


while True:

    print("\nEscolha uma opção:")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar")
    print("4 - Sair")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        cadastrar_cliente(clientes)

    elif opcao == "2":
        listar_clientes(clientes)

    elif opcao == "3":
        buscar_nome(clientes)

    elif opcao == "4":
        print("\nSaindo do sistema de cadastro. Até logo!")
        break

    else:
        print("\nOpção inválida. Tente novamente.\n")