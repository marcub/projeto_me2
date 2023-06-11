class Produto:
    def __init__(self, cod, sku, nome, descricao, preco, categoria, estoque):
        self.__cod = cod
        self.__sku = sku
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__categoria = categoria
        self.__estoque = estoque

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, novo_cod):
        self.__cod = novo_cod

    @property
    def sku(self):
        return self.__sku

    @sku.setter
    def sku(self, novo_sku):
        self.__sku = novo_sku

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self.__descricao = nova_descricao

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, nova_categoria):
        self.__categoria = nova_categoria

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, novo_estoque):
        self.__estoque = novo_estoque

    def __str__(self):
        return (f"Código: {self.cod}\nSKU: {self.sku}\nNome: {self.nome}\nDescrição: {self.descricao}\nPreço: R$ {self.preco:.2f}\nCategoria: {self.categoria}\nEstoque: {self.estoque}")

    def subTotal(self, quantidadeCarrinho):
        return self.preco * quantidadeCarrinho

    def atualizarEstoque(self, quantidade):
        self.estoque -= quantidade
