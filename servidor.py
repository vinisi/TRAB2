import socket
import sys

HOST = '' # Endereco IP do Servidor
PORT = sys.argv[1] # Recebe a porta que o Servidor esta por parametro na linha de comando
udp = socket.socket(socket.AF_INET, #internet
	socket.SOCK_DGRAM) #UDP
orig = (HOST, PORT)
udp.bind(orig)

while True:
	con, cliente = udp.accept()
	print 'Conectado por', cliente
	#Recebe o numero de msgs enviadas pelo cliente
	cont = 1
	num_msg = int (con.recv(1024))
	print 'Recebendo ' + str(num_msg) + ' msgs'
	while cont <=  num_msg:
		msg = con.recv(1024)
		if (msg):
			print 'Recebendo msg '+ str(cont)
			cont = cont + 1
		if not msg:
			break

	print 'Enviando msg de retorno de '+ str (con.send(bytearray(1))) +' para o cliente'
	print 'Finalizando conexao com o cliente', cliente
	con.close()
sys.exit(0)
