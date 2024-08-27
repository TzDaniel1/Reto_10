# Reto_10

### 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```python
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
```

### 2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
```python
x = []
y = []

z = int(input("ingrese la canridad de numeros enteros de los arreglos " ))

for i in range(z):
    w = int(input(f"ingrese numero entero {i+1} del primer arreglo: "))
    x.append(w)

for i in range(z):
    v = int(input(f"ingrese numero entero {i+1} del segundo arreglo: "))
    y.append(v)

print("primer arreglo: ", x)
print("segundo arreglo: ", y)

ProductoPunto = sum(x[i] * y[i] for i in range(z))
print(f"el producto punto de los erreglos es: {ProductoPunto} ")
```

### 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```python
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
```
