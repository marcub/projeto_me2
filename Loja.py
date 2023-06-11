from datetime import date
from LojaException import LojaException

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

    def registrarProduto(self, novoProduto):
        for produto in self.produtos:
            if produto.sku == novoProduto.sku:
                raise LojaException("Erro ao registrar produto: SKU já cadastrado")
        self.produtos.append(novoProduto)

    def removerProduto(self, sku):
        for produto in self.produtos:
            if produto.sku == sku:
                self.produtos.remove(produto)
                break
            else:
                raise LojaException("Falha ao remover produto: SKU não encontrado")

    def registrarCliente(self, novoCliente):
        for cliente in self.clientes:
            if cliente.cpf == novoCliente.cpf:
                raise LojaException("Erro ao registrar cliente: CPF já cadastrado")
        self.clientes.append(novoCliente)

    def removerCliente(self, codigo):
        for cliente in self.clientes:
            if cliente.cod == codigo:
                self.clientes.remove(cliente)
                break
            else:
                raise LojaException("Falha ao remover cliente: código não encontrado")

    def registrarPedido(self, pedido):
        self.pedidos.append(pedido)

    def listarClientes(self):
        for cliente in self.clientes:
            print(cliente)
            print("\n")

    def listarProdutos(self):
        for produto in self.produtos:
            print(produto)
            print("\n")

    def gerarNotaFiscal(self, pedido):
        if pedido in self.pedidos:
            data_atual = date.today().strftime("%d/%m/%Y")
            nota_fiscal = f"Pedido {pedido.cod}\n"
            nota_fiscal += f"Data: {data_atual}\n"
            nota_fiscal += f"Cliente: {pedido.cliente.nome}\n"
            nota_fiscal += f"CPF: {pedido.cliente.cpf}\n"
            nota_fiscal += "Produtos:\n"

            for item in pedido.produtos:
                produto = item
                quantidade = pedido.produtos[item]
                subtotal = item.subTotal(quantidade)
                nota_fiscal += f" - {produto.nome} ({quantidade}x) - R$ {subtotal:.2f}\n"

            nota_fiscal += f"Valor Total: R$ {pedido.calcularTotal():.2f}"
            return nota_fiscal
        else:
            return "Pedido não encontrado!"
