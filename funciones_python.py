print("----------------------------------")
print("-  BUSCAR UN NUMERO EN CONJUNTO  -")
print("----------------------------------")

#Definicion de la funcion
def buscarDatoEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r

#Entrada
dato = int(input("Numero a buscar: ")) #se recibe el dato del usuario

#Procesamiento
lista = [1,2,3,4,5] #Se almacena una lista de datos
if buscarDatoEnLista(dato, lista):
    print("Lo encontre")
else:
    print("No lo encontre")

#Salida
print("\nEso era...")