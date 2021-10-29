from Dominio.ValueObject import ValueObject


class Contraseña(ValueObject[str]):
    def __init__(self, pwd: str) -> None:
        if not pwd.strip():
            raise Exception('La contraseña no puede ser vacía')

        if (len(pwd) < 4 or len(pwd) > 20):
            raise Exception('La contraseña debe tener entre 4 y 20 caracteres')

        super().__init__(pwd)
