class Robot:

	def __init__(self, name=None):
		self.name = name

	def say_hi(self):
		if self.name:
			print("Hi, I am " +self.name)
		else:
			print("I have no name")

	def set_name(self, name):
		self.name = name
	def get_name(self, name):
		return self.name
