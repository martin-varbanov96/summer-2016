class SampleClass():

	def __init__(self, size = 0, color = "Blue"):
		self.size = size
		self.color = color

	def printadin(self):
		print("*" * 10)
		print("This is class with size: {} and color: {}".format(self.size, self.color))
    
	def __str__(self):
		return "This is class with size: {} and color: {}".format(self.size, self.color)

obj_of_sampleCLass = SampleClass()
print(str(obj_of_sampleCLass))
obj_of_sampleCLass.printadin()
