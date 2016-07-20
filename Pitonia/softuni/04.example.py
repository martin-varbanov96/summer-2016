angle = int(input("Enter angle: "));
length = int(input("Enter length: "));

import turtle as t
while True:
	t.left(angle)
	t.forward(length)
	angle+=1