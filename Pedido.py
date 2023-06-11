class Pedido:
    def __init__(self, cod, cliente, dataCompra):
        self.__cod = cod
        self.__cliente = cliente
        self.__dataCompra = dataCompra
        self.__status = "PENDENTE"
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
    def dataCompra(self):
        return self.__dataCompra

    @dataCompra.setter
    def dataCompra(self, novaDataCompra):
        self.__dataCompra = novaDataCompra

    @property
    def status(self):
        return self.__status

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

    def removerItem(self, produto):
        try:
            self.produtos.pop(produto)
        except KeyError:
            print("Erro ao remover: Produto não está no carrinho.")

    def mudarStatus(self):
        self.__status = "CONCLUÍDO"

    def gerarNotaFiscal(self):
            nota_fiscal = f"Pedido {self.cod}\n"
            nota_fiscal += f"Data: {self.dataCompra.strftime('%d/%m/%Y')}\n"
            nota_fiscal += f"Cliente: {self.cliente.nome}\n"
            nota_fiscal += f"CPF: {self.cliente.cpf}\n"
            nota_fiscal += f"Status: {self.status}\n"
            nota_fiscal += "Produtos:\n"

            for item in self.produtos:
                produto = item
                quantidade = self.produtos[item]
                subtotal = item.subTotal(quantidade)
                nota_fiscal += f" - {produto.nome} ({quantidade}x) - R$ {subtotal:.2f}\n"

            nota_fiscal += f"Valor Total: R$ {self.calcularTotal():.2f}"
            return nota_fiscal
