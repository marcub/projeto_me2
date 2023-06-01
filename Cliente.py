class Cliente:
    def __init__(self, cod, nome, cpf, dataDeNascimento, endereco, email, senha):
        self.__cod = cod
        self.__nome = nome
        self.__cpf = cpf
        self.__dataDeNascimento = dataDeNascimento
        self.__endereco = endereco
        self.__email = email
        self.__senha = senha
        self.__carrinho = []

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
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @property
    def dataDeNascimento(self):
        return self.__dataDeNascimento

    @dataDeNascimento.setter
    def dataDeNascimento(self, nova_dataDeNascimento):
        self.__dataDeNascimento = nova_dataDeNascimento

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        self.__email = novo_email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha

    @property
    def carrinho(self):
        return self.__carrinho

    def adicionarCarrinho(self, produto, quantidade):
        self.__carrinho.append((produto, quantidade))

