class Mensagem(object):

    def __init__(self, tipoMSG, idCliente, ordem, checksum):
        self.tipoMSG = tipoMSG
        self.idCliente = idCliente
        self.ordem = ordem
        self.checksum = checksum

    def soma(self):
        return self.tipoMSG + self.idCliente

    def subtrai(self):
        return self.tipoMSG - self.idCliente

    def multiplica(self):
        return self.tipoMSG * self.idCliente

    def divide(self):
        return self.tipoMSG / self.idCliente