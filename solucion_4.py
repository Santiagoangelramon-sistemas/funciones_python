print("---------------------------------------------------")
print("--------- calcula_promedio_lista ------------------------")
print("---------------------------------------------------")

#Definicion de la funcion
def cacular_promedio_lista(lista):
    suma = 0
    for i in lista:
        suma = suma +i
    promedio = suma / len(lista)
    return promedio

# Entrada
# Creamos una lista vacia
lista = []
# Tamoño de la lista
n = int(input("Digite el tamaño de la lista:  "))

for i in range(n):
    num = random.randint(14,18)
    lista.append(num)

#procesamiento
print("Lista: ", lista)
print("La suma es: ". calcular_promedio_lista(lista))

# Salida
print("\nEso era...")