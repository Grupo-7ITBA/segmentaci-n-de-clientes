from Cliente import cliente
import json

class clientesgold(cliente):
    def __init__(self)-> None:
        with open("eventos_gold.json") as jsonFile:
            archivo = json.load(jsonFile)
            jsonFile.close()
            nombres = archivo['nombre'];
            apellidos =archivo['apellido'];
            dni = archivo['dni'];
            tipo =archivo['tipo'];
            numeros =archivo['numero'];

    def puede_crear_chequera(self) -> bool:
        return True

    def puede_crear_tarjeta_de_credito(self) -> bool:
        return True

    def puede_comprar_dolar(self) -> bool:
        return True

    def posee_cuenta_corriente(self) -> bool:
        return True
