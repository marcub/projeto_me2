class Pedido:
    def __init__(self, cod, cliente):
        self.__cod = cod
        self.__cliente = cliente
        self.__produtos = {}

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, novo_cod):
        self.__cod = novo_cod

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, novo_cliente):
        self.__cliente = novo_cliente

    @property
    def produtos(self):
        return self.__produtos

    @produtos.setter
    def produtos(self, novos_produtos):
        self.__produtos = novos_produtos

    def calcularTotal(self):
        total = 0
        for item in self.produtos:
            total += item.subTotal(self.produtos[item])
        return total

    def adicionarItem(self, produto, quantidade):
        self.produtos[produto] = quantidade

    def removerCarrinho(self, produto):
        try:
            self.produtos.pop(produto)
        except KeyError:
            print("Erro ao remover: Produto não está no carrinho.")
