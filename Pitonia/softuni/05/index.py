"""
$ python3    analyze.py   catalog.csv   sales-10K.csv

Обобщение
---------
    Общ брой продажби: 10000
    Общо сума продажби: 3191507.82 €
    Средна цена на продажба: 319.15 €
    Начало на период на данните: 2015-12-01T08:00:48+01:00
    Край на период на данните: 2016-01-24T20:49:38+00:00

Сума на продажби по категории (top 5)
-----------------------------
    SHOES: 1519077.15 €
    T-SHIRTS: 207615.78 €
    HEADWEAR: 176304.77 €
    BALLS: 146092.19 €
    JACKETS: 130226.14 €

Сума на продажби по градове (top 5)
-----------------------------
    Manchester: 100620.74 €
    Liverpool: 96607.68 €
    London: 92239.71 €
    Nottingham: 90084.01 €
    Glasgow: 87052.21 €

Сума на продажби по час (top 5)
-----------------------------
    2015-12-01 12:00:00+01:00: 9209.70 €
    2016-01-17 10:00:00+02:00: 8811.59 €
    2016-01-05 20:00:00+01:00: 8590.52 €
    2015-12-29 20:00:00+02:00: 8270.59 €
    2016-01-05 10:00:00+01:00: 8028.91 €
"""
import operator


def price_overall(sales_dict):
	"""	
    """
	total_amount_variable = 0
	start_date = None
	end_date = None
	for sale in sales_dict:
		total_amount_variable += sale["price"]
		ts = sale["date"]
		if start_date is None or ts < start_date:
			start_date = ts
		if end_date is None or ts > end_date:
			end_date = ts
	print("""

	Обобщение	    

	--------
		Общ брой продажби: {total_sales}
		Общо сума продажби: {total_amount:.2f}
		Средна цена на продажба: {avg_amount:.2f}
		Начало на период на данните: {start_period}
		Край на период на данните: {end_period}
		""".format(total_sales = len(sales_dict), total_amount = total_amount_variable, avg_amount = total_amount_variable/len(sales_dict), start_period = start_date, end_period = end_date))


def price_by_categories(sales, catalog):
	"""
	docs
	"""
	categories_dict = dict()
	for sale in sales:
		current_category = catalog[sale["id"]]
		if current_category not in categories_dict:
			categories_dict[current_category] = sale["price"]
		else:
			categories_dict[current_category] += sale["price"]
	print(categories_dict)
	amounts_sorted = list()
	print("""
	Сума на продажби по категории (top 5)
	-----------------------------""")
	for i in range(0, 5):
		print("""
			SHOES: {:.2f} €
			""".format(23))


def price_by_city():
	"""
	docs
	"""
	pass
def price_by_time():
	"""
	docs
	"""
	pass

def main():
	CATALOG_NAME = "catalog.csv"
	SALES_NAME = "sales-10k.csv"

	from sales import load_sales
	from catalog import load_catalog

	sales_dict = load_sales(SALES_NAME)
	catalog_dicts = load_catalog(CATALOG_NAME)
	price_overall(sales_dict)
	price_by_categories(sales_dict, catalog_dicts)

if __name__ == "__main__":
	main()
