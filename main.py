from Cliente import Cliente
from Produto import Produto
from Loja import Loja
from Pedido import Pedido
from LojaException import LojaException


if __name__ == "__main__":
    
    # Criando alguns produtos
    produto1 = Produto(1, "AR115", "Arroz", "Arroz branco", 10.0, "Alimentos", 50)
    produto2 = Produto(2, "FJ225", "Feijão", "Feijão carioca", 8.0, "Alimentos", 30)
    produto3 = Produto(3, "SB125", "Sabonete", "Sabonete líquido", 5.0, "Higiene", 20)

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
        print('Marketplace'.center(20))
        print('-'*20)
        print("[0] - Loja\n[1] - Cliente\n[2] - Sair")
        escolha = input('-> ')
        if escolha not in escolhas:
            print('Escolha inválida')
            input('Digite qualquer coisa para voltar ao menu: ')
            continue
        if escolha == '1':
            while True:
                print("\n== Bem-vindo(a) a área do cliente ==\n")
                print("[0] - Produtos disponíveis")
                print("[1] - Fazer pedido")
                print("[2] - Voltar")
                opcao = input("\nDigite o número da opção desejada: ")
                print("\n" + "-" * 20)

                if opcao == "0":
                    print("Produtos da loja:\n")
                    loja.listarProdutos()
                    input('Digite qualquer coisa para voltar ao menu: ')

                elif opcao == "1":
                    print("== Fazer Pedido ==")
                    cpfCliente = input("Digite o CPF do cliente: ")

                    for clienteCadastrado in loja.clientes:
                        if clienteCadastrado.cpf == cpfCliente:
                            pedido = Pedido(len(loja.pedidos) + 1, clienteCadastrado)
                            print("Selecione os produtos pelo código (0 para sair): \n")
                            
                            while True:
                                loja.listarProdutos()
                                codigoProduto = int(input("Digite o código do produto: "))

                                if codigoProduto == "0":
                                    break
                                else:
                                    for produto in loja.produtos:
                                        if produto.cod == codigoProduto:
                                            quantidade = int(input("Digite a quantidade desejada: "))
                                            if quantidade == 0:
                                                break
                                            else:
                                                pedido.adicionarItem(produto, quantidade)
                                                break
                                    print("Produto não encontrado.")
                                clienteCadastrado.comprar(pedido, loja)  # Corrigido para passar cliente e pedido separadamente

                            print("\nPedido realizado com sucesso!")
                            print() 
                            print("=== Nota Fiscal ===")
                            print(loja.gerarNotaFiscal(pedido))
                            print()

                        else:
                            print("Cliente não encontrado(a).")
                            print()
                            continue   
                elif opcao == "2":
                    print("VOLTE SEMPRE S2")
                    break
        elif escolha == '0':
            while True:
                print("\n== Bem-vindo(a) ao", loja.nome, "==\n")
                print("[0] - Registrar cliente")
                print("[1] - Remover cliente")
                print("[2] - Registrar produto")
                print("[3] - Remover produto")
                print("[4] - Listar clientes")
                print("[5] - Listar produtos")
                print("[6] - Voltar")
                opcao = input("\nDigite o número da opção desejada: ")
                print("\n" + "-" * 20)

                if opcao == "0":
                    while True:
                        print("== Registro de Novo Cliente ==")
                        nome = input("Nome: ")
                        cpf = input("CPF: ")
                        data_nascimento = input("Data de nascimento: ex(03022000)") ##TRANSFORMAR EM DATE, E MOSTRAR FORMATADO
                        endereco = input("Endereço: ")
                        email = input("Email: ") ##VALIDAÇÃO POR BIBLIOTECA
                        senha = input("Senha: ") ##TEM QUE SER MAIOR QUE 5 CARACTERES E MENOR QUE 255

                        novo_cliente = Cliente(len(loja.clientes) + 1, nome, cpf, data_nascimento, endereco, email, senha)
                        try:
                            loja.registrarCliente(novo_cliente)
                        except LojaException as Err:
                            print("\n" + Err.msg)
                        else:
                            print("\nCliente registrado com sucesso!")
                        input('\nDigite qualquer coisa para voltar ao menu: ')
                        break
                elif opcao == "1":
                    codigo_cliente = int(input("Digite o código do cliente que deseja remover: "))
                    try:
                        loja.removerCliente(codigo_cliente)
                    except LojaException as Err:
                        print("\n" + Err.msg)
                    else:
                        print("\nCliente removido com sucesso!")
                    input('\nDigite qualquer coisa para voltar ao menu: ')
                elif opcao == "2":
                    while True:
                        print("== Registro de Novo Produto ==")
                        sku = input("SKU: ")
                        nome = input("Nome: ")
                        descricao = input("Descrição: ")
                        preco = float(input("Preço: R$ "))
                        categoria = input("Categoria: ")
                        estoque = int(input("Estoque: "))
                        novo_produto = Produto(len(loja.produtos) + 1, sku, nome, descricao, preco, categoria, estoque)
                        try:
                            loja.registrarProduto(novo_produto)
                        except LojaException as Err:
                            print("\n" + Err.msg)
                        else:
                            print("\nProduto registrado com sucesso!")
                        input('\nDigite qualquer coisa para voltar ao menu: ')
                        break
                elif opcao == "3":
                    sku_produto = input("Digite o SKU do produto que deseja remover: ")
                    try:
                        loja.removerProduto(sku_produto)
                    except LojaException as Err:
                        print("\n" + Err.msg)
                    else:
                        print("\nProduto removido com sucesso!")
                    input('\nDigite qualquer coisa para voltar ao menu: ')
                elif opcao == "4":
                    print("Clientes da loja:\n")
                    loja.listarClientes()
                    input('Digite qualquer coisa para voltar ao menu: ')
                elif opcao == "5":
                    print("Produtos da loja:\n")
                    loja.listarProdutos()
                    input('Digite qualquer coisa para voltar ao menu: ')
                elif opcao == "6":
                        break
        elif escolha == '2':
            print('Obrigado!')
            break