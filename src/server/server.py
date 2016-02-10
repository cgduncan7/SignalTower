import socket
import sys
import time

HOST, PORT = "localhost", 9999
ADDRESS = (HOST, PORT)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDRESS)
server_socket.listen(1)

while True:
	print "Listening for client..."
	conn, address = server_socket.accept()
	print "Client connected: ", address

	while True:
		output = conn.recv(2048)
		if output.strip() == "disconnect":
			conn.send("dack")
			conn.close()
			break
		elif output:
			print "Message received from client: ", output
			conn.send("ack")