import math

a = float(input("Informe A número: "))
b = float(input("Informe B número: "))
c = float(input("Informe C número: "))

if a == 0:
    print("'A' deve ser diferente de 0.")
else:

    x = (b ** 2) - 4 * a * c

    if x < 0:
        print("A equação não possui raízes reais.")
    else:
        raizX = math.sqrt(x)
        r1 = (-b + raizX) / (2 * a)
        r2 = (-b - raizX) / (2 * a)

        if r1 == r2:
            print("Equação de uma raiz real: x = ", r1)
        else:
            print(f"As raízes da equação são: x1 = {r1}, x2 = {r2}")
