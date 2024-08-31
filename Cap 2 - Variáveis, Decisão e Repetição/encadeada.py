
nome=input("Digite seu nome: ")
idade=int(input("Digite a idade: "))
doencaCont=input("Suspeita de doença contagiosa? ").upper()
print('--------RECEBENDO DADOS--------')

if idade>=60:
    print('O paciente: ' + nome + ' possui atendimento prioritário!')

if idade<=18:
    print('O paciente: ' + nome + 'é menor de idade!')

else:
    print('O paciente ' + nome + ' está no atendimento regular')


if doencaCont=="SIM":
    print('Paciente ' + nome+ '  deve ser direcionado a sala de espera isolada URGENTE!')

else:
    print('O paciente ' + nome + ' não apresentou sintomas de doença contagiosa')

print('Atendimento encerrado! :D')