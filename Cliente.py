import re
from datetime import datetime

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class Cliente:
    def __init__(self, cod, nome, cpf, dataDeNascimento, endereco, email, senha):
        self.__cod = cod
        try:
            if len(nome) != 0:
                self.__nome = nome
            else:
                raise ValueError
        except ValueError:
            print("Erro ao registrar cliente: nome inválido")
            raise
        try:
            if len(cpf) == 11 and cpf.isdigit():
                self.__cpf = cpf
            else:
                raise ValueError
        except ValueError:
            print("Erro ao registrar cliente: CPF inválido")
            raise
        try:
            self.__dataDeNascimento = datetime.strptime(dataDeNascimento, "%d/%m/%Y").date()
        except ValueError:
            print("Erro ao registrar cliente: data de nascimento inválida")
            raise
        else:
            try:
                if datetime.strptime(dataDeNascimento, "%d/%m/%Y").date() < datetime.now().date():
                    self.__dataDeNascimento = datetime.strptime(dataDeNascimento, "%d/%m/%Y").date()
                else:
                    raise ValueError
            except ValueError:
                print("Erro ao registrar cliente: data de nascimento no futuro") 
                raise   
        self.__endereco = endereco
        try:
            if re.search(regex, email):
                self.__email = email
            else:
                raise ValueError
        except ValueError:
            print("Erro ao registrar cliente: email inválido")
            raise
        try:
            if len(senha) > 5 and len(senha) < 255:
                self.__senha = senha
            else:
                raise ValueError
        except ValueError:
            print("Erro ao registrar cliente: senha deve conter entre 5 e 255 caracteres")
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
        return (f"Código: {self.cod}\nNome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.dataDeNascimento.strftime('%d/%m/%Y')}\nEndereço: {self.endereco}\nEmail: {self.email}")

    def adicionarPedido(self, pedido):
        self.__pedidos.append(pedido)

    def listarPedidos(self):
        for pedido in self.pedidos:
            print(pedido.gerarNotaFiscal())
            print("\n")

