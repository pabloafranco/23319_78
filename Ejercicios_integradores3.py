
#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def crearDiccionario(cadena):
    diccio = {}
    palabras = cadena.split()
    for i in palabras:
        if i in diccio:
            diccio[i] += 1
        else:
            diccio[i] = 1

            
    return diccio

print(crearDiccionario("Esto es una prueba de muchas cosas de todas las pruebas que hicimos esto es lo mejor de todas las pruebas"))