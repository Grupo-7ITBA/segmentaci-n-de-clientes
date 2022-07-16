
class Direccion:

    def __init__(self, direccion):
        self.calle = direccion['calle']
        self.numero = direccion['numero']
        self.ciudad = direccion['ciudad']
        self.provincia = direccion['provincia']
        self.pais = direccion['pais']

    def output_as_label(self):
        return f"<label>{self.calle} N° {self.numero}, {self.ciudad}, {self.provincia}, {self.pais}</label>"
