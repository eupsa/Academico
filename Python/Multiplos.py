num = int(input("Informe um número: "))

while (num != -1):
    if num > 10:
        i = 0
        for i in range(1, num + 1):
            if num % i == 0:
                print(i)
            if i == num:
                num = int(input("Informe um número: "))
    else:
        print("Número inválido.")
        num = int(input("Informe um número: "))