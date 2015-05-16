import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
try:
	PORT = int(sys.argv[1]) # Arbitrary non-privileged port
except:
	print 'Informe a porta [servidor].py [porta]'
	sys.exit()
 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    print 'Informe o tipo de cliente'
    d = s.recvfrom(1024)
    if type(d) is not int:
    	s.sendto('Informe o tipo do cliente' , addr)
    else:
    	if d == 0:
    		print 'Emissor conectado'

    	e = s.recvfrom(1024)
		data = e[0]
		addr = e[1]
	     
	    if not data: 
	        break
	     
	    reply = 'OK...' + data
	     
	    s.sendto(reply , addr)
	    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip() 
s.close()