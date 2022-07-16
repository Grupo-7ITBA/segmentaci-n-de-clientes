
class Razon:

    def __init__(self, cliente, evento):
        self.razon = self.resolver(cliente, evento)

    @staticmethod
    def resolver(cliente, evento):
        tipo_evento = evento['tipo']
        match tipo_evento:
            case 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                return RazonRetiroEfectivo.validacion(evento, cliente)


class RazonRetiroEfectivo:

    @staticmethod
    def validacion(evento, cliente):
        if evento['monto'] < cliente.cuenta.limite_extraccion_diario:
            if not evento['monto'] <= evento['cupoDiarioRestante']:
                return f"""La cantidad supera el cupo diario de retiros,
                        solo puede retirar ${evento['cupoDiarioRestante']}. """
            elif evento['monto'] > evento['saldoEnCuenta']:
                return f"No tienes fondos suficientes."
        else:
            return f"Excede el monto de MÁXIMO de ${cliente.cuenta.limite_extraccion_diario}"
