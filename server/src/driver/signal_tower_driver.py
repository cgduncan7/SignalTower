# import RPi.GPIO as GPIO

from ..properties.constant import CONSTANT

# Holds constants for each module; replace
class Modules(object):

	@CONSTANT
	def GREEN_LIGHT():
		return "GREEN_LIGHT"

	@CONSTANT
	def GREEN_LIGHT_GPIO_PORT():
		return 1

	@CONSTANT
	def RED_LIGHT():
		return "RED_LIGHT"

	@CONSTANT
	def RED_LIGHT_GPIO_PORT():
		return 2
	
	@CONSTANT
	def SIREN():
		return "SIREN"

	@CONSTANT
	def SIREN_GPIO_PORT():
		return 3

class Driver(object):
	"""
	Driver for siren modules; receives commands from SignalTowerServer
	"""
	def __init__(self):
		super(Driver, self).__init__()
		self.modules = SirenModules()