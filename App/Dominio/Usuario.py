from Dominio.Contraseña import Contraseña
from Dominio.Correo import Correo
from Dominio.Nombre import Nombre
from Dominio.Apellido import Apellido
from Dominio.Edad import Edad
from Dominio.Sexo import Sexo


class Usuario:
    def __init__(self,
                 correo: Correo,
                 contraseña: Contraseña,
                 nombre: Nombre,
                 apellido: Apellido,
                 edad: Edad,
                 sexo: Sexo,
                 ) -> None:
        self.correo = correo
        self._contraseña = contraseña
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def esContraseñaValida(self, pwd: str) -> bool:
        return self._contraseña.validar(pwd)

    def nombreCompleto(self) -> str:
        return "{0}, {1}".format(self.apellido, self.nombre)

