print("----------------------------------")
print("-  BUSCAR UN NUMERO EN CONJUNTO  -")
print("----------------------------------")

# Entrada

b = int(input("Numero a buscar: ")) # Se recibe el dato del usuario

# Procesamiento

a = [1,2,3,4,5] # se almacena una lista de datos
r = False # se inicia la variable r con un valor falso

for i in a:
    if i== b:

        print("Lo encontre")
        r = True
if r==False:
    print("No lo encontre")

# salida

print("Eso no era")