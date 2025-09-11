import time

i = 0

print("Contagem regressiva!\n")
for i in range(10, -1, -1):
    print(f"{i}")
    time.sleep(1)
