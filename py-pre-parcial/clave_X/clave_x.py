import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma(numero1, numero2):
    return numero1+numero2


"""
***************************************************************
@@ ejercicio 2 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*5 = 40
"""


# start-->
def multiplicacion(numero1, numero2, numero3):
    return numero1*numero2*numero3


"""
***************************************************************
@@ ejercicio 3 @@
un metodo python que haga la suma de los numeros de la lista
numerosLista = [2,5,4,6,9,12]
"""


# start-->
def sumarLista(mylist):
    suma=0
    for elementos in range(len(mylist)):
        suma += mylist[elementos]
    return suma


"""
***************************************************************
@@ ejercicio 4 @@
colocar este proyecto en github
colocar aca debajo la url
enviar la url al correo balbino_a@hotmail.com
"""


# github url-->
def getGithubUrl():
    return "https://github.com/victoriaZepeda/Preparcial.git"
