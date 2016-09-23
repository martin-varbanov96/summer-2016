class Parent:
	def __init__(self, size = 0, age = 53):
		self.age = age
		self.size = size
		

	def __str__(self):
		return "This parent has size: {size}, and age: {age}".format(size = self.size, age = self.age)

class Child(Parent):
	def __init__(self, size = 5, age = 51, height = 150):
		super().__init__(size, age)
		self.height = height

	def __str__(self):
		return "This child has size: {size}, and age: {age} and also height: {height}".format(size = self.size, age = self.age, height = self.height)

def main():
	parent_class = Parent()
	son_class = Child()
	print(str(parent_class))
	print("*" * 20)
	print(str(son_class))

main()