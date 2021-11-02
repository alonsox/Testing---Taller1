from Dominio.Altura import Altura
from Dominio.Peso import Peso
from Dominio.Sexo import Sexo

class IMC:
    def __init__(self, altura: Altura, peso: Peso, sexo: Sexo) -> None:
        # CALCULA IMC
        valor_imc = round(peso/altura**2,1)

        if sexo == 'F':
            if valor_imc < 20:
                print('Bajo peso')
            elif valor_imc > 20 and valor_imc <= 23.9:
                print('Normal')
            elif valor_imc > 23.9 and valor_imc <= 28.9:
                print('Obesidad leve')
            elif valor_imc > 28.9 and valor_imc <= 37:
                print('Obesidad severa')
            else:
                print('Obesidad muy severa')
        if sexo == 'M':
            if valor_imc < 20:
                print('Bajo peso')
            elif valor_imc > 20 and valor_imc <= 24.9:
                print('Normal')
            elif valor_imc > 24.9 and valor_imc <= 29.9:
                print('Obesidad leve')
            elif valor_imc > 29.9 and valor_imc <= 40:
                print('Obesidad severa')
            else:
                print('Obesidad muy severa')

        super().__init__(nombre)
