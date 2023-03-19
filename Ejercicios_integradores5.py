"""
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
"""

def get_int():
    nuevo_numero=0
    while nuevo_numero==0:
        
        numero=input("Ingrese un numero:")
        print (f"El numero ingresado es {numero}.")
        try:
            nuevo_numero=int(numero)
            return nuevo_numero

        except ValueError:
            print ("Dato Invalido")

def get_int_r():
    nuevo_numero=0
        
    numero=input("Ingrese un numero:")
    print (f"El numero ingresado es {numero}.")
    try:
        nuevo_numero=int(numero)
        return nuevo_numero

    except ValueError:
        print ("Dato Invalido")
        get_int_r()

    
    
get_int_r()
