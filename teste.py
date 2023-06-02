from Produto import Produto
from Pedido import Pedido
from Cliente import Cliente

if __name__ == "__main__":
    produto1 = Produto(1, "Arroz", "Arroz branco", 10.0, "Alimentos", 50)
    produto2 = Produto(2, "Feijão", "Feijão carioca", 8.0, "Alimentos", 30)
    produto3 = Produto(3, "Sabonete", "Sabonete líquido", 5.0, "Higiene", 20)

    marcus = Cliente("1525", "Marcus", "0215484", "15/05/2320", "msasaijdjiajid", "dsodokskdos", "1524")

    produtos = {produto1:2, produto2:3}

    pedido1 = Pedido("2514", marcus)
    pedido1.adicionarItem(produto1, 2)
    pedido1.adicionarItem(produto3, 4)

    print(pedido1.gerarNotaFiscal())

    pedido1.removerCarrinho(produto2)

    print(pedido1.gerarNotaFiscal())