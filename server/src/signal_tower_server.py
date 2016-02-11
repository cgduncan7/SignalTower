import socket
import sys
import time

class Server(object):
	"""
	Class which handles all network communication to and fro
	the Signal Tower.
	"""
	
	def __init__(self, host, port, verbose):
		super(Server, self).__init__()
		self.host = host
		self.port = port
		self.verbose = verbose
		self.address = (host, port)
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Wrapper for print to only print if verbose == True
	def _print(self, val):
		if self.verbose:
			print val

	# Generic bind() wrapped to handle exceptions
	def bind(self, socket, address):
		try:
			socket.bind(address)
			self._print("Socket bound...")
		except Exception, e:
			print "Error binding to socket"
			exit(1)

	# Generic listen() wrapped to handle exceptions
	def listen(self, socket):
		try:
			socket.listen(1)
			self._print("Listening for 1 client...")
			
			conn, address = socket.accept()
			self._print("Accepted client connection...")

		except Exception, e:
			print e
			print "Error listening for clients"
			exit(1)
		else:
			return (conn, address)

	# Generic recv() wrapped to handle exceptions
	def recv(self, conn, size):
		try:
			msg = conn.recv(size)
			self._print("Received message from client... %s" % msg)
		except Exception, e:
			print "Error receiving message from client"
			exit(1)
		else:
			return msg

	# Generic send() wrapped to handle exceptions
	def send(self, conn, msg):
		try:
			conn.send(msg)
			self._print("Sending message to client... %s" % msg)
		except Exception, e:
			print "Error sending message to client"
			exit(1)

	# Generic close() wrapped to handle exceptions
	def close(self, conn):
		try:
			conn.close()
			self._print("Closing connection...")
		except Exception, e:
			print "Error closing connection"
			exit(1)

	# Sends an ack msg to conn
	def ack_client(self):
		self.send(self.conn, "ack")

	# Sends a dack msg to conn
	def dack_client(self):
		self.send(self.conn, "dack")

	# Notifies client of disconnect and closes socket
	def disconnect_client(self):
		self.all_off()
		self.dack_client()
		self.conn.close()

	# Turns all modules off
	def all_off(self):
		# TODO
		pass

	# Turns all modules on
	def all_on(self):
		# TODO
		pass

	def echo(self, msg):
		self.send(self.conn, msg)

	# Parses the messages from client and acts accordingly
	def parse(self, message):
		if message == "disconnect":
			self.disconnect_client()
		else:
			self.echo(message)

		
	def start(self):
		self.bind(self.socket, self.address)
		self.conn, self.address = self.listen(self.socket)

		while self.conn is not None:
			message = self.recv(self.conn, 2048)
			self.ack_client()
			self.parse(message)
		
# OLD::
# HOST, PORT = "localhost", 9999
# ADDRESS = (HOST, PORT)

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(ADDRESS)
# server_socket.listen(1)

# while True:
# 	print "Listening for client..."
# 	conn, address = server_socket.accept()
# 	print "Client connected: ", address

# 	while True:
# 		output = conn.recv(2048)
# 		if output.strip() == "disconnect":
# 			conn.send("dack")
# 			conn.close()
# 			break
# 		elif output:
# 			print "Message received from client: ", output
# 			conn.send("ack")