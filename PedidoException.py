class PedidoException(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)
    def __str__(self):
        return self.msg