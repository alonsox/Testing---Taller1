from Pantallas.PantallaHandler import PantallaHandler
from Utilidades.Otros import limpiarPantalla
from Dominio.Usuario import Usuario


class CalcularImcHandler(PantallaHandler):
    def handle(self, usuario: Usuario) -> None:
        limpiarPantalla()
        print('Calculando IMC para [' + usuario.correo() + ']', end='\n\n')
        input('Presiona enter para volver al menu principal...')
        self.next()
