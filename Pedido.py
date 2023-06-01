from Produto import Produto
from datetime import date

class Pedido:
    def __init__(self, cod, cliente, produtos):
        self.__cod = cod
        self.__cliente = cliente
        self.__produtos = produtos

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
        total = 0.0
        for produto in self.produtos:
            total += produto.preco
        return total

    def adicionarItem(self, produto, quantidade):
        item = {'produto': produto, 'quantidade': quantidade}
        self.produtos.append(item)

    def removerCarrinho(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            produto.quantidadeCarrinho -= 1
            if produto.quantidadeCarrinho < 0:
                produto.quantidadeCarrinho = 0

    def calcularTotal(self):
        total = 0

        for item in self.produtos:
            produto = item['produto']
            quantidade = item['quantidade']
            subtotal = quantidade * produto.preco
            total += subtotal

        return total

    def gerarNotaFiscal(self):
        data_atual = date.today().strftime("%d/%m/%Y")
        nota_fiscal = f"Pedido {self.cod}\n"
        nota_fiscal += f"Data: {data_atual}\n"
        nota_fiscal += f"Cliente: {self.cliente.nome}\n"
        nota_fiscal += f"CPF: {self.cliente.cpf}\n"
        nota_fiscal += "Produtos:\n"

        for item in self.produtos:
            produto = item['produto']
            quantidade = item['quantidade']
            subtotal = quantidade * produto.preco
            nota_fiscal += f" - {produto.nome} ({quantidade}x) - R${subtotal:.2f}\n"

        nota_fiscal += f"Valor Total: R${self.calcularTotal():.2f}"

        return nota_fiscal
