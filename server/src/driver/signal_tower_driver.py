from gpiozero import OutputDevice

class Driver(object):
	"""
	Driver for siren modules; receives commands from SignalTowerServer
	"""
	def __init__(self, green_pin, red_pin, siren_pin):
		super(Driver, self).__init__()
		self.green_light = OutputDevice(green_pin)
		self.red_light = OutputDevice(red_pin)
		self.siren = OutputDevice(siren_pin)

	def exec_instr(self, instruction):
		if instruction[0]:
			self.green_light.on()
		else:
			self.green_light.off()

		if instruction[1]:
			self.red_light.on()
		else:
			self.red_light.off()

		if instruction[2]:
			self.siren.on()
		else:
			self.siren.off()