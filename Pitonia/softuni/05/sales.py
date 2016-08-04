#!!! MUST use CHCP 65001 before using program

import csv
import iso8601

CATALOG_NAME = "catalog.csv"
SALES_NAME = "sales-10k.csv"



def load_sales(file_name):
	SALES_ID = 0
	SALES_COUNTRY = 1
	SALES_CITY = 2
	SALES_DATE = 3
	SALES_PRICE =4
	"""
	00.Идентификационен номер на артикула;
	01.Държава, в която е била извършена продажбата (ISO code)
	02.Име на град, в която е била извършена продажбата;
	03.Дата/час на продажбата с timezone, във формат ISO8601;
	04.Цена на продажбата (цените на един и същ артикул в различните държави са различни)
	
	Result:
		list of dicts [ 
			{
				id - JSAD!@#
				city - Gorna
				date - datetime(2015, 23, 123, ...)
				price - 123,4
			}
		]
	"""
	with open(file_name,  'r', newline='', encoding='utf8') as r:
		reader = csv.reader(r)
		result=[]
		for row in reader:
			sale={}
			sale["id"]=row[SALES_ID]
			sale["country"]=row[SALES_COUNTRY]
			sale["city"]=row[SALES_CITY] #[i.encode('ascii', 'ignore').decode('ascii') for i in row..
			sale["date"]=row[SALES_DATE]
			sale["price"]=float(row[SALES_PRICE])
			result.append(sale)
		return result