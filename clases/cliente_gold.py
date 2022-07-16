import json
from cliente import Cliente


class Gold(Cliente):

    def __init__(self) -> None:
        with open("eventos_gold.json") as jsonFile:
            archivo = json.load(jsonFile)
            jsonFile.close()
            super().__init__(archivo, {'limite_extraccion_diario': 20000, 'limite_transferencia_recibida': 500000,
                                       'costo_transferencia': 0.5})

    def puede_crear_chequera(self, cant_chequeras) -> bool:
        if cant_chequeras >= 1:
            return False
        else:
            return True

    def puede_crear_tarjeta_de_credito(self, cant_tarjetas) -> bool:
        if cant_tarjetas >= 1:
            return False
        else:
            return True

    def puede_comprar_dolar(self) -> bool:
        return True

    def posee_cuenta_corriente(self) -> bool:
        return True
