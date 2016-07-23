input_str = input("Enter string = ")
filter_str = input("Enter filter = ")
if(input_str.find(filter_str) >= 0):
	print(input_str[input_str.find(filter_str)+ len(filter_str) :] )