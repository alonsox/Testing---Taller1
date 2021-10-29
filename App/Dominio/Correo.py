from Dominio.ValueObject import ValueObject

class Correo(ValueObject[str]):
    def __init__(self, correo: str) -> None:
        if not correo.strip():
            raise Exception('El correo no puede estar vacío')
    
        super().__init__(correo)
