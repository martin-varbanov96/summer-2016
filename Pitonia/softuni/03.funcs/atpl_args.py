CONST_VAL = 25

# * creates a tuple of all the input arguments
def arg_tpl(*args):
	print(args)
def cubic(num):
	return num ** num
def get_constval(num):
	return num * CONST_VAL

arg_tpl(2, 3, 4, 5)
print(cubic(4))
print(get_constval(23))
