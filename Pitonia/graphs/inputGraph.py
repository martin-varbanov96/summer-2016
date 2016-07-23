import math
import matplotlib.pyplot as plt 

func_form = input("Enter func = ")
start = int(input("Enter start = "))
end = int(input("Enter end = "))

x_axis = [];
y_axis = [];

def func_y(x , func_form):
	return eval(func_form)

for x in range(start, end):
	x_axis.append(x);
	y_axis.append(func_y(x, func_form));

plt.plot(x_axis, y_axis)
plt.show()

input("Press Enter to continue...")
