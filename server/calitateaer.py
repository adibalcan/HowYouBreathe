import requests
import harddata
from pyquery import PyQuery as pq
from pprint import pprint

url = 'http://www.calitateaer.ro/valori.php'
r = requests.post(url, data = harddata.requestdata)
dom = pq(r.text)
data = dom('#afis_date > td > table:nth-child(1) tr')
indexRow=1

values = {}
cities = {}

for row in data:
	line = pq(row).find('td')
	indexColumn = 1
	for column in line:
		if indexColumn == 1:
			indexColumn += 1
			continue

		value = pq(column).text().strip()

		if indexRow == 1:
			# print(value)
			city = harddata.statii[value]['city']
			cities[str(indexColumn)] = city 
			
			values[city] = {"codname":value}

		if indexRow == 3:
			city = cities[str(indexColumn)]
			values[city]['monoxid_carbon'] = value

		indexColumn += 1
	indexRow += 1

pprint(values)
# print(r.text.encode("utf-8"))
input()