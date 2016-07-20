import turtle
side=50
for i in range(8):
	if i % 2 ==0:
		for i in range(8):
			if i % 2==0:
				turtle.begin_fill()
				for i in range(0, 4):
					turtle.forward(side)
					turtle.left(90)
			turtle.end_fill()
			if( i == 7):
				turtle.right(90)
				turtle.forward(side)
				turtle.right(90)
			turtle.forward(side)
	else:
		for i in range(8):
			if i % 2==0:
				turtle.begin_fill()
				for i in range(0, 4):
					turtle.forward(side)
					turtle.right(90)
			turtle.end_fill()
			if( i == 7):
				turtle.left(90)
				turtle.forward(side)
				turtle.left(90)
			turtle.forward(side)


turtle.exitonclick()