z = []

y = int(input("Ingrese la cantidad de numeros reales que desea agregar al arreglo: "))

for i in range(y):
    x = float(input(f"Ingrese el numero real {i+1}: "))
    z.append(x)

print("su arreglo es:", z)

if y > 0:
    promedio = sum(z)/y
    print("el promedio es:", promedio)
else:
    print("")