import socket
import time

HOST, PORT = "localhost", 9999
ADDRESS = (HOST,PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDRESS)
connected = True

while connected:
	msg = raw_input("$>")

	if msg != "":

		client_socket.send(msg)

		print "Waiting for ack."

		while client_socket.recv(2048) != "ack":
			pass

		print "Ack received."
	
	else:
		print "Disconnecting."
		connected = False
		client_socket.send("disconnect")

		print "Waiting for dack."

		while client_socket.recv(2048) != "dack":
			pass

		print "Dack received."

		client_socket.shutdown(socket.SHUT_RDWR)
		client_socket.close()