import csv
def load_catalog(file_name):
	CATALOG_ID = 0
	CATALOG_CAT = 5
	"""
	Columns:
	Идентификационен номер на артикула;
	Наименование на артикула;
	Цветове, в които артикулът е наличен;
	Група на артикула;
	Спорт, за който е предназначен артикулът;
	Категория
	Подкатегория
	Пол, за който е предназначен артикула - мъже, жени, unisex, деца, бебета
	return dict dict[ID] = catagory
	"""
	with open(file_name, 'r', encoding="utf-8") as f:
		reader = csv.reader(f)
		result = {}
		for row in reader:
			result[row[CATALOG_ID]] = row[CATALOG_CAT]
		return result
