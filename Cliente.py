class Cliente:
    def __init__(self, cod, nome, cpf, dataDeNascimento, endereco, email, senha):
        self.__cod = cod
        self.__nome = nome
        self.__cpf = cpf
        self.__dataDeNascimento = dataDeNascimento
        self.__endereco = endereco
        self.__email = email
        self.__senha = senha
        self.__pedidos = []

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
    def pedidos(self):
        return self.__pedidos
    
    def __str__(self):
        return (f"Código: {self.cod}\nNome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.dataDeNascimento}\nEndereço: {self.endereco}\nEmail: {self.email}")

    def adicionarPedido(self, pedido):
        self.__pedidos.append(pedido)

    def comprar(self, pedido, loja):
        for item in pedido.produtos:
            produto = item
            quantidade = pedido.produtos[item]
            if produto in loja.produtos:
                if produto.estoque >= quantidade:
                    produto.atualizarEstoque(quantidade)
                else:
                    print(f"Não há estoque suficiente para o produto {produto.nome}")
            else:
                print(f"O produto não está disponível na loja.")
        loja.registrarPedido(pedido)

