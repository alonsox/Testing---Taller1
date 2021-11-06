from Pantallas.Pantalla import Pantalla
from Dominio.Usuario import Usuario
from Dominio.Altura import Altura
from Dominio.Peso import Peso
from Dominio.IMC import IMC
from Utilidades.Otros import tryWhileError
from datetime import datetime


class CalcularImc(Pantalla):
    def mostrar(self, usuario: Usuario) -> None:
        # LEER LOS DATOS DEL USUARIO
        self.limpiar()
        print(f'CALCULANDO IMC PARA: {usuario.nombreCompleto()}', end='\n\n')
        print(f'Ingrese los datos que se le piden a continuación.', end='\n\n')

        altura = tryWhileError(lambda: Altura(input("Altura (Metros): ")))
        peso = tryWhileError(lambda: Peso(input("Peso (Kg): ")))
        fecha_peso = tryWhileError(self._leerFecha)

        # MOSTRAR RESULTADOS
        self.limpiar()
        calculadoraIMC = IMC(altura, peso, usuario.sexo)
        print('RESULTADOS DEL CÁLCULO DE IMC', end='\n\n')

        print('DATOS PERSONALES')
        print(f'Nombre: {usuario.nombreCompleto()}')
        print(f'Edad  : {usuario.edad}')
        print(f'Sexo  : {usuario.sexo}')
        print(f'Fecha : {fecha_peso.strftime("%a %d/%m/%Y")}')
        print(f'Hora  : {fecha_peso.strftime("%I:%M %p")}', end='\n\n')

        print('RESULTADOS IMC')
        print(f'Peso  : {altura} Kg')
        print(f'Altura: {peso} m')
        print(f'IMC   : {calculadoraIMC.calcularIMC()}')
        print(f'Estado: {calculadoraIMC.evaluarIMC().upper()}', end='\n\n')

        input('Presione ENTER para volver al menu principal...')
        self.navegar('menu_logueado', usuario)

    def _leerFecha(self):
        try:
            fecha = str(input('Fecha y hora del peso [dd/mm/yyyy hh:mm]: '))
            return datetime.strptime(fecha, "%d/%m/%Y %H:%M")
        except:
            raise Exception('Formato inválido.')
