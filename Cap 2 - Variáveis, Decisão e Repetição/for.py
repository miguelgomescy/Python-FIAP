tabuada=int(input("Digite um número: "))
print('Tabuada do número ',tabuada)

for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor)+ " = " + str((tabuada*valor)))