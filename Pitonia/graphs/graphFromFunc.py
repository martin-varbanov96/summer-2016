
# def getFunction( start, finish, func):
# 	for x in range(start, finish):


x_axis = [];
y_axis = [];

def func_y(x):
	return 5 - 5*x/3

for x in range(-10, 10):
	x_axis.append(x);
	y_axis.append(func_y(x));

import matplotlib.pyplot as plt 
plt.plot(x_axis, y_axis)
plt.show()

input("Press Enter to continue...")
