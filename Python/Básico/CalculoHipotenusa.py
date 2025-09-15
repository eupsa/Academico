import math

a = int(input("Informe o Cateto Adjacente: "))
b = int(input("Informe o Cateto Oposto: "))

# total = math.hypot(a, b)

total = math.sqrt(a**2 + b**2)

print(total)