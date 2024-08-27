arreglo = []

n = int(input("Ingrese la cantidad de elementos en el arreglo: "))

print("Ingrese los elementos del arreglo:")
for i in range(n):
    elemento = float(input(f"Elemento {i+1}: "))
    arreglo.append(elemento)

arreglo_sin_ceros = [num for num in arreglo if num != 0]
cantidad_ceros = arreglo.count(0)
arreglo_reorganizado = arreglo_sin_ceros + [0] * cantidad_ceros

print("El arreglo reorganizado es:", arreglo_reorganizado)