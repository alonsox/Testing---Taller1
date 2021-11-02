from Dominio.ValueObject import ValueObject


class Edad(ValueObject[int]):
    def __init__(self, edad: int) -> None:
        # VALIDAR QUE SEA UN NUMERO ENTERO
        if type(edad) != type(1):
            raise Exception('La edad debe ser un número entero')

        # VALIDAR QUE LA EDAD ESTE EN RANGO PERMITIDO
        if edad < 15 or edad > 70:
            raise Exception('La edad debe estar entre 15 y 70 años')

        super().__init__(edad)
