# -*- coding: utf-8 -*-
# lesson 3.5: common files formats: CSV, JSON

import csv
'''
with open("module3/example.csv") as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)
print("")
with open("module3/example.tsv") as f:
	reader = csv.reader(f, delimiter="\t")
	for row in reader:
		print(row)
students = [
	["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
	["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]
'''
'''
with open("module3/example.csv", "a") as f:
	writer = csv.writer(f)
	for student in students:
		writer.writerow(student)
'''
'''
with open("module3/example.tsv", "a") as f:
	writer = csv.writer(f, delimiter="\t")
	for student in students:
		writer.writerow(student)
'''
'''
with open("module3/example.csv", "a") as f:
	writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
	writer.writerows(students)
'''
# Example 1
'''
import csv
crimes = []
with open("Crimes.csv") as f:
	reader = csv.reader(f)
	for row in reader:
		date = row[2]
		if date[6:10] == "2015":
			crimes.append(row)
primares = []
for row in crimes:
	primares.append(row[6])
count_primares = dict((x, primares.count(x)) for x in set(primares) if primares.count(x) > 1)
keys_list = list()
for i in count_primares.keys():
	keys_list.append(i)
minimal = count_primares[keys_list[0]]
for key in count_primares.keys():
	if count_primares[key] > minimal:
		minimal = count_primares[key]
		name = key
print(name, minimal)
'''
# Example 2
import csv
from collections import Counter
primares = []
with open("Crimes.csv") as f:
		for row in csv.reader(f):
			if row[2][6:10] == "2015":
				primares.append(row[6])
print(Counter(primares).most_common()[0][0])