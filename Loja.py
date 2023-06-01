class Loja:
    def __init__(self, nome, cnpj, produtos, clientes, pedidos):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__produtos = produtos
        self.__clientes = clientes
        self.__pedidos = pedidos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.__cnpj = novo_cnpj

    @property
    def produtos(self):
        return self.__produtos

    @produtos.setter
    def produtos(self, novos_produtos):
        self.__produtos = novos_produtos

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clientes(self, novos_clientes):
        self.__clientes = novos_clientes

    @property
    def pedidos(self):
        return self.__pedidos

    @pedidos.setter
    def pedidos(self, novos_pedidos):
        self.__pedidos = novos_pedidos

    def registrarProduto(self, produto):
        self.produtos.append(produto)

    def removerProduto(self, cod):
        for produto in self.produtos:
            if produto.cod == cod:
                self.produtos.remove(produto)
                break

    def registrarCliente(self, cliente):
        self.clientes.append(cliente)

    def removerCliente(self, cod):
        for cliente in self.clientes:
            if cliente.id == cod:
                self.clientes.remove(cliente)
                break

    def registrarPedido(self, pedido):
        self.pedidos.append(pedido)

    def listarClientes(self):
        for cliente in self.clientes:
            print(cliente.nome)

    def listarProdutos(self):
        for produto in self.produtos:
            print(produto.nome)

    def comprar(self, cliente, pedido):
        for item in pedido.produtos:
            produto = item['produto']
            quantidade = item['quantidade']
            if produto in self.produtos:
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                    produto.quantidadeCarrinho += quantidade
                    cliente.adicionarCarrinho(produto, quantidade)
                else:
                    print(f"Não há estoque suficiente para o produto {produto.nome}")
            else:
                print(f"O produto {produto.nome} não está disponível na loja.")
