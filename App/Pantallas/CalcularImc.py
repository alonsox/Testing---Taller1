from Pantallas.Pantalla import Pantalla
from Utilidades.Otros import limpiarPantalla
from Dominio.Usuario import Usuario


class CalcularImc(Pantalla):
    def mostrar(self, usuario: Usuario) -> None:
        limpiarPantalla()
        print('Calculando IMC para [' + usuario.correo() + ']', end='\n\n')
        input('Presiona enter para volver al menu principal...')
        self.navegar('menu_deslogueado')
