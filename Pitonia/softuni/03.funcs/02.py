input_file = open("./catalog_full.csv", 'r')
gender_dic = {"Kid" : 0, "Infant" : 0, "Woman" : 0, "Men" : 0 , "Unisex" : 0}
gender_count = {"Kid" : 0, "Infant" : 0, "Woman" : 0, "Men" : 0 , "Unisex" : 0}
for line in input_file:
	line = line.split(',')
	gender_dic[line[5]] += float(line[6])
	gender_count[line[5]] += 1
input_file.close()
for element in gender_dic:
	gender_dic[element] = gender_dic[element]/float(gender_count[element])
print(gender_dic)