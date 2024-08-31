def perguntar():
    return ("O que deseja realizar? \n" +
               "<I> - Inserir novo usuário \n" +
               "<P> - Pesquisar um usuário \n" +
               "<E> - Excluir usuário" +
               "<L> - Listar usuário: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
                                                      input("Digite a última data de acesso: "), 
                                                      input("Qual a ultima estação acessada: ").upper()]
    
def salvar(dicionário):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionário.items():
            arquivo.write(chave+":"+str(valor))