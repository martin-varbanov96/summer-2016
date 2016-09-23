import csvkit
reader = csvkit.reader('sales-10k.csv')
for row in reader:
	print(row)