from Dominio.Contraseña import Contraseña
from Dominio.Correo import Correo


class Usuario:
    def __init__(self, correo: Correo, contraseña: Contraseña) -> None:
        self._correo = correo
        self._contraseña = contraseña

    def esContraseñaValida(self, pwd: str) -> bool:
        return self._contraseña.validar(pwd)

    def correo(self) -> str:
        return self._correo.valor()
