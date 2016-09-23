def get_avg():
	input_file = open("./catalog_full.csv", 'r')
	sum = 0
	count = 0
	for line in input_file:
		count += 1
		line = line.split(',')
		sum += float(line[-1])
	input_file.close()
	return sum / float(count)

print(get_avg())