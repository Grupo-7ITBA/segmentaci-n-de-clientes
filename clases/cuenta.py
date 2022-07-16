from razones import Razon


class Cuenta:

    def __init__(self, datos_cuenta, transacciones) -> None:
        self.limite_extraccion_diario = datos_cuenta['limite_extraccion_diario']
        self.limite_transferencia_recibida = datos_cuenta['limite_transferencia_recibida']
        self.costo_transferencia = datos_cuenta['costo_transferencia']
        self.razones = self.__transacciones_rechazadas(transacciones)

    def __transacciones_rechazadas(self, transacciones):
        transacciones_r = [transaccion for transaccion in transacciones if transaccion['estado'] == 'RECHAZADO']
        razones = [Razon(self, transaccion) for transaccion in transacciones_r]
        return razones
