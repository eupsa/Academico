nomeCompleto = input("Infomre um nome completo: ")

print("\n")
print("Maíusculo: ", nomeCompleto.upper())
print("Minúsculo: ",nomeCompleto.lower())
print("Sem espaço: ",nomeCompleto.replace(" ", ""))
print("Tamanho sem espaço: ", len(nomeCompleto.replace(" ", "")))