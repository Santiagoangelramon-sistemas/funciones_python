# Construir una funcion que reciba como parametro una lista  de datos numericos y retorne el promedio de los datos pares

print("---------------------------------------------------")
print("--------- Datos Numericos Par/Impar ---------------")
print("---------------------------------------------------")

def promedio_pares(lista_numeros):

    # Entrada: Creamos una lista vacía para almacenar los números pares
    pares = []

    # Procedimiento: Filtramos los números pares
    for num in lista_numeros:
        if num % 2 == 0:
            pares.append(num)

    # Procedimiento: Verificamos si hay números pares
    if not pares:
        return 0

    # Procedimiento: Calculamos la suma y el conteo de los números pares
    suma_pares = sum(pares)
    conteo_pares = len(pares)

    # Procedimiento: Calculamos el promedio
    promedio = suma_pares / conteo_pares

    # Salida: Retornamos el promedio
    return promedio

# Ejemplo de uso
lista_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
promedio = promedio_pares(lista_ejemplo)
print("El promedio de los números pares es:", promedio)