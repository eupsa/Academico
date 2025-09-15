a = int(input("1º lado do trianqulo: "))
b = int(input("2º lado do trianqulo: "))
c = int(input("3º lado do trianqulo: "))

if a == b and c == b: # ou a==b==c
    print("O triangulo é equilátero ")
elif a == b and b != c:
    print("O triangulo é Isósceles")
else:
    print("O triangulo é Escaleno")