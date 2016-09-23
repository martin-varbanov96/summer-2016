import matplotlib.pyplot as plt 
import math

class Figure:
	def __init__(self, figure_x = 0, figure_y = 0, radius = 0):
		self.figure_x = figure_x
		self.figure_y = figure_y
		self.radius = radius

	def __str__(self):
		return "Figure is at {x}:{y} with radius = {rad}".format(x = self.figure_x, y = self.figure_y, rad = self.radius)

class Circle(Figure):
	def __init__(self, figure_x = 0, figure_y = 0, radius = 0):
		super().__init__(figure_x, figure_y, radius)

	def draw_graph(self):
		x_axis = [];
		y_axis = [];
		x0 = self.figure_x
		y0 = self.figure_y
		x = self.radius
		y = 0
		err = 0
		rad = self.radius

		x_axis.append(self.figure_x)
		y_axis.append(self.figure_y)

		while(x >= y):
			x_axis.append(x0 + x)
			y_axis.append(y0 + y)

			x_axis.append(x0 + y)
			y_axis.append(y0 + x)

			x_axis.append(x0-y)
			y_axis.append(y0 + x)

			x_axis.append(x0 - x)
			y_axis.append(y0 + y)

			x_axis.append(x0 - x)
			y_axis.append(y0 - y)

			x_axis.append(x0 - y)
			y_axis.append(y0 - x)
			
			x_axis.append(x0 + y)
			y_axis.append(y0 - x)
			
			x_axis.append(x0 + x)
			y_axis.append(y0 - y)

			y += 1;
			err += 1 + 2*y;
			if (2*(err-x) + 1 > 0):
				x -= 1;
				err += 1 - 2*x;

		plt.scatter(x_axis, y_axis)
		plt.show()

class Square(Figure):
	"""docstring for Square"""
	def __init__(self, figure_x = 0, figure_y = 0, radius = 0, distance = 10):
		super().__init__(figure_x, figure_y, radius)
		self.distance = distance

	def draw_graph(self):
		x_axis = [];
		y_axis = [];

		for left_side_y in range(self.figure_y, self.distance):
			x_axis.append(self.figure_x);
			y_axis.append(left_side_y)

		for right_side_x in range(self.figure_x+1, self.distance):
			x_axis.append(right_side_x)
			y_axis.append(self.distance-1)

			x_axis.append(right_side_x)
			y_axis.append(self.figure_y)

		for right_side_y in range(self.figure_y, self.distance):
			x_axis.append(self.distance)
			y_axis.append(right_side_y)

		plt.scatter(x_axis, y_axis)
		plt.show()

		
def main():
	samepl_square = Square(2, 3, 5)
	sample_circle = Circle(10, 10, 3000)
	print(str(samepl_square))
	print("*"*30)
	print(str(sample_circle))
	sample_circle.draw_graph()


main()
		
