num = int(input("Informe um número: "))

i = 0
fatorial = 1

for i in range(num, 0, -1):
    fatorial*=i
print(fatorial)