# Construir una funcion que reciba como parametro una lista numerica y rentorne la suma de dichos datos.

print("---------------------------------------------------")
print("--------- SUMA LISTA DATOS ------------------------")
print("---------------------------------------------------")

#Definicion de la funcion
def sumar_lista_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma 

# Entrada
# Creamos una lista vacia
lista = []
# Tamoño de la lista
n = int(input("Digite el tamaño de la lista:  "))

for i in range(n):
    num = random.randit(1,9)
    lista.append(num)

# Procedimiento
print("Lista: ", lista)
print("La suma es: ". suma_lista_datos(lista))

# Salida
print("\nEso era...")