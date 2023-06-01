from Cliente import Cliente
from Produto import Produto
from Loja import Loja
from Pedido import Pedido

# Criando alguns produtos
produto1 = Produto(1, "Arroz", "Arroz branco", 10.0, "Alimentos", 50)
produto2 = Produto(2, "Feijão", "Feijão carioca", 8.0, "Alimentos", 30)
produto3 = Produto(3, "Sabonete", "Sabonete líquido", 5.0, "Higiene", 20)

# Criando alguns clientes
cliente1 = Cliente(1, "João", "12345678900", "01/01/1990", "Rua A, 123", "joao@email.com", "senha")
cliente2 = Cliente(2, "Maria", "98765432100", "05/05/1995", "Rua B, 456", "maria@email.com", "senha")

# Criando a loja
produtos = [produto1, produto2, produto3]
clientes = [cliente1, cliente2]
pedidos = []  # Lista vazia de pedidos
loja = Loja("Mercadinho", "123456789", produtos, clientes, pedidos)

while True:
    print("== Bem-vindo(a) ao", loja.nome, "==")
    print("Opções:")
    print("1. Listar produtos")
    print("2. Listar clientes")
    print("3. Registrar cliente")
    print("4. Remover produto da loja")
    print("5. Fazer pedido")
    print("0. Sair")
    print("-" * 20)

    opcao = input("Digite o número da opção desejada: ")
    print("-" * 20)

    if opcao == "1":
        print("Produtos da loja:")
        loja.listarProdutos()
        print()

    elif opcao == "2":
        print("Clientes da loja:")
        loja.listarClientes()
        print()

    elif opcao == "3":
        print("== Registro de Novo Cliente ==")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de nascimento: ")
        endereco = input("Endereço: ")
        email = input("Email: ")
        senha = input("Senha: ")

        novo_cliente = Cliente(len(clientes) + 1, nome, cpf, data_nascimento, endereco, email, senha)
        loja.registrarCliente(novo_cliente)
        print("Cliente registrado com sucesso!")
        print()

    elif opcao == "4":
        codigo_produto = input("Digite o código do produto que deseja remover: ")
        loja.removerProduto(int(codigo_produto))
        print("Produto removido com sucesso!")
        print()

    elif opcao == "5":
        print("== Fazer Pedido ==")
        cpf_cliente = input("Digite o CPF do cliente: ")
        cliente = None

        for c in clientes:
            if c.cpf == cpf_cliente:
                cliente = c
                break

        if cliente is None:
            print("Cliente não encontrado.")
            print()
            continue

        pedido = Pedido(len(loja.pedidos) + 1, cliente, [])
        print("Selecione os produtos pelo código (0 para sair):")
        
        while True:
            loja.listarProdutos()
            codigo_produto = input("Digite o código do produto: ")

            if codigo_produto == "0":
                break

            produto_encontrado = None

            for produto in loja.produtos:
                if produto.cod == int(codigo_produto):
                    produto_encontrado = produto
                    break

            if produto_encontrado is None:
                print("Produto não encontrado.")
                continue

            quantidade = int(input("Digite a quantidade desejada: "))

            if quantidade == 0:
                break

            pedido.adicionarItem(produto_encontrado, int(quantidade))

        
        loja.registrarPedido(pedido)
        loja.comprar(cliente, pedido)  # Corrigido para passar cliente e pedido separadamente
        print("Pedido realizado com sucesso!")
        print()
        print("=== Nota Fiscal ===")
        print(pedido.gerarNotaFiscal())
        print()
    
    elif opcao == "0":
        print("VOLTE SEMPRE S2")
        break
