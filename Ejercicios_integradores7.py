"""
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.
"""

class Cuenta():
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad

    def __str__(self):
        return f'Titular: {self.__titular}  Cantidad: {self.__cantidad}'

    #GETTER
    @property
    def titular(self):
        return self.__titular

    #SETTER
    @titular.setter
    def nombre(self,nuevo_titular):
        self.__titular  = nuevo_titular

    def mostrar(self):
        print(f'Titular: {self.__titular}  \nCantidad: {self.__cantidad}')

    def ingresar(self, cantidad):
        try:
            if cantidad<0:
                print("No se puede ingresar una cantidad negativa")
            else:
                self.__cantidad += cantidad
        except:
            print (f'Valor incorrecto {cantidad}')


    def retirar(self, cantidad):
        try:
            self.__cantidad -= cantidad
        except:
            print (f'Valor incorrecto {cantidad}')
"""
nueva_cuenta=Cuenta('Pablo')
nueva_cuenta.ingresar(20)
nueva_cuenta.mostrar()
nueva_cuenta.ingresar("adsasdf")
nueva_cuenta.retirar(50)
nueva_cuenta.mostrar()
"""
nueva_cuenta=Cuenta('Pablo')
nueva_cuenta.retirar("34234")
