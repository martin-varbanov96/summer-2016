input_file = open("./catalog_full.csv", 'r')
output_file = open("./catalog_full_updated.csv", 'w')
for line in input_file:
	line = line.split(',')
	line[-1] = float("{0:.2f}".format(float(line[-1]) * 1.75))
	for idi, i in enumerate(line):
		output_file.write(str(line[idi]))
		if(line[idi] is not line[-1]):
			output_file.write(",")
		else:
			output_file.write("\n")
output_file.close()
input_file.close()
