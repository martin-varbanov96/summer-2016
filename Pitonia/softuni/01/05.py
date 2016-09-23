angle = int(input("Enter angle: "));
length = int(input("Enter length: "));
oboroti = int(input("Enter times: "));

import turtle as t


for i in range(0, oboroti):
	t.left(angle)
	t.forward(length)
	angle+=1