i = 0
soma = 0

for i in range(1, 7):
    num = int(input(f"Informe o {i}º número: "))

    if num % 2 == 0:
       soma+=num
print(soma)