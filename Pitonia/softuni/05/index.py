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
from datetime import datetime, timezone
import iso8601


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
	sorted_categories = sorted(categories_dict.items(), key=operator.itemgetter(1))
	print("""
	Сума на продажби по категории (top 5)
	-----------------------------""")
	for i in range(0, 5):
		print("""
			{}: {:.2f} €
			""".format(sorted_categories[-1-i][0], sorted_categories[-1-i][1]))


def price_by_city(sales_dict):
	"""
	docs
	"""
	city_price_dict = dict()
	for sale in sales_dict:
		city = sale["city"]
		price = sale["price"]
		if city not in city_price_dict:
			city_price_dict[city] = 0
		city_price_dict[city] += price
		sorted_cities = sorted(city_price_dict.items(), key=operator.itemgetter(1))
	print("""

				Сума на продажби по градове (top 5)
				-----------------------------
		""")
	for i in range(0, 5):
			print("""
					{city}: {price:.2f} €
						""".format(city = sorted_cities[-1-i][0], price = sorted_cities[-1-i][1]))


def price_by_time(sales):
	"""
	Сума на продажби по час (top 5)
-----------------------------
	2015-12-01 12:00:00+01:00: 9209.70 €
	2016-01-17 10:00:00+02:00: 8811.59 €
	2016-01-05 20:00:00+01:00: 8590.52 €
	2015-12-29 20:00:00+02:00: 8270.59 €
	2016-01-05 10:00:00+01:00: 8028.91 €

	input: sales->dictionary
	output: None
	printing info from above
	"""
	date_dict = dict()
	for sale in sales:
		current_date_utc = iso8601.parse_date(sale["date"]).astimezone(timezone.utc)
		current_date_utc = current_date_utc.replace(minute=0, second=0, microsecond=0)   # с точност до час
		if current_date_utc not in date_dict:
			date_dict[current_date_utc] = 0
		date_dict[current_date_utc] += sale["price"]
	sorted_dict = sorted(date_dict.items(), key=operator.itemgetter(1))
	print("""

	Сума на продажби по час (top 5)
-----------------------------
		""")
	for i in range(0, 5 ):
		print("{date}: {price:.2f} €".format(date=str(sorted_dict[-i-1][0]), price=sorted_dict[-i-1][1]))


def main():
	CATALOG_NAME = "catalog.csv"
	SALES_NAME = "sales-10k.csv"

	from sales import load_sales
	from catalog import load_catalog

	sales_dict = load_sales(SALES_NAME)
	catalog_dicts = load_catalog(CATALOG_NAME)
	price_overall(sales_dict)
	price_by_categories(sales_dict, catalog_dicts)
	price_by_city(sales_dict)
	price_by_time(sales_dict)

if __name__ == "__main__":
	main()
