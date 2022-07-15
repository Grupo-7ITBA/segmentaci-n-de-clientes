class Cliente:
    def __init__(self):
        self.cuenta = cuenta; 
        self.nombre = nombre; #Esto viene dado por el archivo del profe
        self.apellido = apellido; #Esto viene dado por el archivo del profe
        self.numero = numero; #Esto viene dado por el archivo del profe
        self.dni= dni;
       
    
    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_de_credito(self) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False

    def posee_cuenta_corriente(self) -> bool:
        return False
    
    def costo_transfernecia(self, monto: int) -> int:
