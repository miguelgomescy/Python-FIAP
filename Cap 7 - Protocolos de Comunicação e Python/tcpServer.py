from socket import *

servidor = "127.0.0.1" # localhost
porta=43210

obj_socket = socket(AF_INET, SOCK_STREAM) #tipo de identificação do servidor #sock para trabalhar com tcp
obj_socket.bind((servidor,porta))
obj_socket.listen(2)

print('Aguardando cliente...')

while True:
    con, cliente = obj_socket.accept()
    print('Conectado com: ', cliente)
    while True:
        msg_recebida = str(con.recv(1024)) #quantidade bytes que espera-se receber na msg
        print('Recebemos: ', msg_recebida)
        msg_enviada = b'Olah Cliente'
        con.send(msg_enviada)
        break
    con.close()
