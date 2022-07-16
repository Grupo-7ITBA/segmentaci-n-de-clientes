class Cuenta:
    
    def __init__(self, datos_cuenta) -> None:
        self.limite_extraccion_diario = datos_cuenta['limite_extraccion_diario']
        self.limite_transferencia_recibida = datos_cuenta['limite_transferencia_recibida']
        self.costo_transferencia = datos_cuenta['costo_transferencia']
