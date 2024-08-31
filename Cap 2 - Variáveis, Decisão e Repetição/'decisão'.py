
nome=input("Digite seu nome: ")
idade=int(input("Digite a idade: "))

if idade>=60:
    print('O paciente: ' + nome + ' possui atendimento prioritário!')

if idade<=18:
    print('O paciente: ' + nome + 'é menor de idade!')

else:
    print('O paciente ' + nome + ' está no atendimento regular')

print('Atendimento encerrado! :D')