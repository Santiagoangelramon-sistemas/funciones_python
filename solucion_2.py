def mostrar_cadena_n_veces():
  """
  Esta función solicita al usuario una cadena y un número n, y luego muestra la cadena n veces.
  """

  cadena = input("Ingresa una cadena: ")
  n = int(input("Ingresa un número entero: "))

  for _ in range(n):
    print(cadena)

# Llama la función para ejecutarla
mostrar_cadena_n_veces()