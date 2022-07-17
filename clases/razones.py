
class Razon:

    def __init__(self, cuenta, evento):
        self.razon = self.resolver(cuenta, evento)

    @staticmethod
    def resolver(cuenta, evento):
        tipo_evento = evento['tipo']
        match tipo_evento:
            case 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                return RazonRetiroEfectivo.validacion(evento, cuenta)


class RazonRetiroEfectivo:

    @staticmethod
    def validacion(evento, cuenta):
        if evento['monto'] < cuenta.limite_extraccion_diario:
            if not evento['monto'] <= evento['cupoDiarioRestante']:
                return f"""La cantidad supera el cupo diario de retiros,
                        solo puede retirar ${evento['cupoDiarioRestante']}. """
            elif evento['monto'] > evento['saldoEnCuenta']:
                return f"No tienes fondos suficientes."
        else:
            return f"Excede el monto de MÁXIMO de ${cuenta.limite_extraccion_diario}"


class RazonAltaChequera:

    @staticmethod
    def validacion(evento, cliente):
        if not cliente.puede_crear_chequera(evento['totalChequerasActualmente']):
            if evento['totalChequerasActualmente'] == 0:
                return "El cliente no puede crear chequeras"
            else:
                return "El cliente no puede crear mas chequeras"
