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
escolhas = ['0', '1', '2']
while True:
    print('-'*20)
    print('Sistema de Loja'.center(20))
    print('-'*20)
    print("[0] para Loja\n[1] para Cliente\n[2] Sair")
    escolha = input('->')
    if escolha not in escolhas:
        print('Escolha inválida')
        input('Digite qualquer coisa para voltar ao menu: ')
        continue
    if escolha == '1':
        while True:
            print("== Bem-vindo(a) ao", loja.nome, "==")
            print("Opções:")
            print("0. Listar produtos")
            print("1. Fazer pedido")
            print("2. Voltar")
            print("-" * 20)

            opcao = input("Digite o número da opção desejada: ")
            print("-" * 20)

            if opcao == "0":
                print("Produtos da loja:")
                try:
                    loja.listarProdutos()
                    input('Digite qualquer coisa para voltar ao menu: ')
                except:
                    pass

            elif opcao == "1":
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
            
            elif opcao == "2":
                print("VOLTE SEMPRE S2")
                break
    elif escolha == '0':
        while True:
            print("== Bem-vindo(a) ao", loja.nome, "==")
            print("0. Registrar cliente")
            print("1. Remover produto da loja")
            print("2. Listar clientes")
            print("3. Voltar")
            opcao = input("Digite o número da opção desejada: ")
            print("-" * 20)

            if opcao == "0":
                while True:
                    print("== Registro de Novo Cliente ==")
                    nome = input("Nome: ")
                    cpf = input("CPF: ")
                    data_nascimento = input("Data de nascimento: ex(03022000)") ##TRANSFORMAR EM DATE, E MOSTRAR FORMATADO
                    endereco = input("Endereço: ")
                    email = input("Email: ") ##VALIDAÇÃO POR BIBLIOTECA
                    senha = input("Senha: ") ##TEM QUE SER MAIOR QUE 5 CARACTERES E MENOR QUE 255

                    novo_cliente = Cliente(len(clientes) + 1, nome, cpf, data_nascimento, endereco, email, senha)
                    try:
                        loja.registrarCliente(novo_cliente)
                    except:
                        print("Erro criando cliente, tente novamente")
                        continue
                    print("Cliente registrado com sucesso!")
                    input('Digite qualquer coisa para voltar ao menu: ')
                    break

            elif opcao == "1":
                    codigo_produto = input("Digite o código do produto que deseja remover: ")
                    try:
                        loja.removerProduto(int(codigo_produto))
                    except:
                        print('Erro ao remover produto, tente novamente')
                        continue
                    print("Produto removido com sucesso!")
                    input('Digite qualquer coisa para voltar ao menu: ')

            elif opcao == "2":
                    print("Clientes da loja:")
                    try:
                        loja.listarClientes()
                        input('Digite qualquer coisa para voltar ao menu: ')
                    except:
                        pass

            elif opcao == "3":
                    break
    elif escolha == '2':
        print('Obrigado!')
        break