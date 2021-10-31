import csv
import os
from typing import Union
from Dominio.Contraseña import Contraseña
from Dominio.Correo import Correo
from Dominio.RepositorioUsuarios import RepositorioUsuarios
from Dominio.Usuario import Usuario


class RepositorioUsuariosCSV(RepositorioUsuarios):
    def __init__(self, rutaArchivo: str) -> None:
        self._rutaArchivo: str = rutaArchivo

        # CREAR ARCHIVO SI NO EXISTE
        if not os.path.exists(self._rutaArchivo):
            # Crea directorios padre
            os.makedirs(os.path.dirname(self._rutaArchivo))

            # Escribe las cabeceras
            with open(self._rutaArchivo, mode='a') as archivoUsuarios:
                writer = csv.writer(archivoUsuarios)
                writer.writerow(['correo', 'contraseña'])

    def guardar(self, usuario: Usuario) -> None:
        # VERIFICA QUE EL CORREO NO ESTE EN USO
        correo = usuario.correo()
        if self.buscar(correo):
            raise Exception(
                'El usuario con correo {0} ya existe'.format(correo))

        # GUARDA EL USUARIO
        with open(self._rutaArchivo, mode='a') as archivoUsuarios:
            writer = csv.writer(archivoUsuarios)

            writer.writerow([usuario.correo(), usuario._contraseña.valor()])

    def buscar(self, correo: str) -> Union[Usuario, None]:
        with open(self._rutaArchivo, mode='r') as archivoUsuarios:
            reader = csv.DictReader(archivoUsuarios)

            for row in reader:
                if (row['correo'] == correo):
                    return Usuario(Correo(row['correo']), Contraseña(row['contraseña']))
