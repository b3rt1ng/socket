def send(message, port, ip):
	import socket
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.connect((ip, port))
	socket.send(bytes(message, 'utf-8'))
	socket.close()

try:
	send("ceci est un message", 1555, "localhost")
except:
	print('erreur, serveur injoignable')