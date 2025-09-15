idade = int(input("Informe uma idade: "))

if idade < 16:
    print("n pode votar")
elif idade >= 18 and idade < 70:
    print("Seu voto é obrigatório.")
else:
    print("Seu voto é facultativo.")