
import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 1555))

def traitement(truc):
	decoded = truc.decode('utf-8')
	return(decoded)

while True:
        socket.listen(5)
        client, address = socket.accept()
        print('connecté à ', address)
        response = client.recv(255)
        if response != "":
        		print(traitement(response))

print(fermeture)
client.close()
stock.close()
"""
def serveur(port):
	def traitement(ordre):
		decoded = ordre.decode('utf-8')
		return(decoded)
	import socket
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind(('', 15555))
	while True:
		socket.listen(5)
		client, address = socket.accept()
		print('connecté à ', address)
		response = client.recv(255)
        if response != "": 
        	print(traitement(response))
    client.close()
	stock.close()
serveur(15555)
"""
