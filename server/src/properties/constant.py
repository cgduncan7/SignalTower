# Constant property

def CONSTANT(f):
	def fset(self, value):
		raise TypeError

	def fget(self):
		return f()

	return property(fget, fset)