from Funcoes import *

usuarios = {}
opcao = perguntar()
opcao = input("O que deseja realizar? \n" +
               "<I> - Inserir novo usuário \n" +
               "<P> - Pesquisar um usuário \n" +
               "<E> - Excluir usuário \n" +
               "<L> - Listar usuário: ").upper()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    opcao = perguntar()
    salvar()