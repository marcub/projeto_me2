from Cliente import Cliente
from Produto import Produto
from Loja import Loja
from Pedido import Pedido
from LojaException import LojaException
import time
from datetime import datetime

if __name__ == "__main__":
    
    # Criando alguns produtos
    produto1 = Produto(1, "AR115", "Arroz", "Arroz branco", 10.0, "Alimentos", 50)
    produto2 = Produto(2, "FJ225", "Feijão", "Feijão carioca", 8.0, "Alimentos", 30)
    produto3 = Produto(3, "SB125", "Sabonete", "Sabonete líquido", 5.0, "Higiene", 20)

    # Criando alguns clientes
    cliente1 = Cliente(1, "João", "12345678900", "01/01/1990", "Rua A, 123", "joao@email.com", "senha1")
    cliente2 = Cliente(2, "Maria", "98765432100", "05/05/1995", "Rua B, 456", "maria@email.com", "senha2")

    # Criando alguns pedidos
    pedido1 = Pedido(1, cliente1, datetime.now())
    pedido1.adicionarItem(produto1, 5)
    pedido1.adicionarItem(produto2, 4)
    cliente1.adicionarPedido(pedido1)

    pedido2 = Pedido(2, cliente2, datetime.now())
    pedido2.adicionarItem(produto3, 5)
    pedido2.adicionarItem(produto1, 1)
    pedido2.adicionarItem(produto2, 4)
    cliente2.adicionarPedido(pedido2)

    # Criando a loja
    produtos = [produto1, produto2, produto3]
    clientes = [cliente1, cliente2]
    pedidos = [pedido1, pedido2]
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
            cpfCliente = input("Digite o CPF do cliente: ")
            for clienteCadastrado in loja.clientes:
                if clienteCadastrado.cpf == cpfCliente:
                    while True:
                        print("\n== Bem-vindo(a) a área do cliente ==\n")
                        print("[0] - Produtos disponíveis")
                        print("[1] - Fazer pedido")
                        print("[2] - Listar Pedidos")
                        print("[3] - Voltar")
                        opcao = input("\nDigite o número da opção desejada: ")
                        print("\n" + "-" * 20)
                        if opcao == "0":
                            print("Produtos da loja:\n")
                            loja.listarProdutos()
                            input('Digite qualquer coisa para voltar ao menu: ')
                        elif opcao == "1":
                            print("== Fazer Pedido ==")

                            pedido = Pedido(len(loja.pedidos) + 1, clienteCadastrado, datetime.now())
                            print("Selecione os produtos pelo código (0 para sair): \n")
                            time.sleep(1)
                            
                            while True:
                                loja.listarProdutos()
                                codigoProduto = int(input("Digite o código do produto: "))

                                if codigoProduto == 0 and len(pedido.produtos) == 0:
                                    break
                                elif codigoProduto < 0:
                                    print("Insira um valor válido")
                                    time.sleep(1)
                                    break
                                elif codigoProduto == 0 and len(pedido.produtos) > 0:
                                    pedido.mudarStatus()
                                    clienteCadastrado.adicionarPedido(pedido)
                                    loja.registrarPedido(pedido)
                                    print("\nPedido realizado com sucesso!")
                                    print("=== Nota Fiscal ===")
                                    print(pedido.gerarNotaFiscal())
                                    time.sleep(1)
                                    break
                                else:
                                    for produto in loja.produtos:
                                        if produto.cod == codigoProduto:
                                            quantidade = int(input("Digite a quantidade desejada: "))
                                            if quantidade <= 0:
                                                print("Quantidade inválida")
                                                time.sleep(1)
                                                break
                                            elif quantidade > produto.estoque:
                                                print("Estoque insuficiente para compra")
                                                time.sleep(1)
                                                break
                                            else:
                                                pedido.adicionarItem(produto, quantidade)
                                                produto.atualizarEstoque(quantidade)
                                                break
                                    else:
                                        print("Produto não encontrado.")
                                        time.sleep(1)
                                        break
                            break
                        elif opcao == "2":
                            print("Pedidos:\n")
                            clienteCadastrado.listarPedidos()
                            input('Digite qualquer coisa para voltar ao menu: ')
                        elif opcao == "3":
                            print("VOLTE SEMPRE S2")
                            break
                    break
            else:
                print("\nCliente não encontrado(a).\n")    
        elif escolha == '0':
            while True:
                print("\n== Bem-vindo(a) ao", loja.nome, "==\n")
                print("[0] - Registrar cliente")
                print("[1] - Remover cliente")
                print("[2] - Registrar produto")
                print("[3] - Remover produto")
                print("[4] - Listar clientes")
                print("[5] - Listar produtos")
                print("[6] - Listar pedidos")
                print("[7] - Voltar")
                opcao = input("\nDigite o número da opção desejada: ")
                print("\n" + "-" * 20)

                if opcao == "0":
                    while True:
                        print("== Registro de Novo Cliente ==")
                        nome = input("Nome: ")
                        cpf = input("CPF: ")
                        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ") 
                        endereco = input("Endereço: ")
                        email = input("Email: ")
                        senha = input("Senha: ")

                        try:
                            novo_cliente = Cliente(len(loja.clientes) + 1, nome, cpf, data_nascimento, endereco, email, senha)
                        except ValueError:
                            break

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
                    print("Pedidos da loja:\n")
                    loja.listarPedidos()
                    input('Digite qualquer coisa para voltar ao menu: ')
                elif opcao == "7":
                        break
        elif escolha == '2':
            print('Obrigado!')
            break