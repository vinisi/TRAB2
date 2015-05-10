import socket
import sys
import time

HOST	 = '10.0.0.1' 	# Endereco IP do Servidor
PORT = sys.argv[1]	# Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, #internet
	socket.SOCK_DGRAM) #UDP
dest = (HOST, PORT)
udp.connect(dest)
cont = 1
num_msg = 5000
tam_msg = bytearray(1000)

#informa ao servidor quantas msg serao enviadas
udp.send (num_msg)

inicio = time.time()
while cont <= num_msg:
	if udp.send (tam_msg):
		print 'Enviando msg '+ str(cont) + 'de ' + str(sys.getsizeof(bytearray(1000))) + 'B'
		cont = cont + 1

print 'Recebendo msg de ' + str(sys.getsizeof(bytearray(udp.recv(1)))) + 'B'
fim = time.time() - inicio
print 'Tempo total de execucao' + str (fim)
udp.close()
print 'Encerrando conexao com o servidor'
sys.exit(0)
