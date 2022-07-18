import json
from clases.cliente import Cliente


class Classic(Cliente):

    def __init__(self) -> None:
        with open("data/eventos_classic.json") as jsonFile:
            archivo = json.load(jsonFile)
            jsonFile.close()
            super().__init__(archivo, {'limite_extraccion_diario': 10000, 'limite_transferencia_recibida': 150000,
                                       'costo_transferencia': 1})

    def get_cuenta(self):
        super(Classic, self).get_cuenta()

    def puede_crear_chequera(self, cant_chequeras) -> bool:
        return False

    def puede_crear_tarjeta_de_credito(self, cant_tarjetas) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False

    def posee_cuenta_corriente(self) -> bool:
        return True
