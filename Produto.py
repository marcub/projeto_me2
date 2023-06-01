class Produto:
    def __init__(self, cod, nome, descricao, preco, categoria, estoque):
        self.__cod = cod
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__categoria = categoria
        self.__quantidadeCarrinho = 0
        self.__estoque = estoque

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, novo_cod):
        self.__cod = novo_cod

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
    def quantidadeCarrinho(self):
        return self.__quantidadeCarrinho

    @quantidadeCarrinho.setter
    def quantidadeCarrinho(self, nova_quantidade):
        self.__quantidadeCarrinho = nova_quantidade

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, novo_estoque):
        self.__estoque = novo_estoque

    @property
    def quantidade(self):
        return self.__estoque

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self.__estoque = nova_quantidade

    def subTotal(self):
        return self.preco * self.quantidadeCarrinho

    def atualizarCarrinho(self, quantidade):
        self.quantidadeCarrinho = quantidade
