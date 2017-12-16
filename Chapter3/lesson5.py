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
import csv, re, collections
primares = list()
with open("Crimes.csv", "r") as file:
	reader = csv.DictReader(file)
	for row in reader:
		row = dict(row)
		if "2015" in re.findall(r"\d\d/\d\d/(\d\d\d\d) \d\d:\d\d:\d\d", row["Date"]):
			primares.append(row["Primary Type"])
print(collections.Counter(primares).most_common()[0])
'''
import json
student1 = {
	"first_name": "Greg",
	"last_name": "Dean",
	"scores": [70, 80, 90],
	"description": "Good job, Greg",
	"certificate": True
}

student2 = {
	"first_name": "Wirt",
	"last_name": "Wood",
	"scores": [80, 80.2, 80],
	"description": "Nicely Done",
	"certificate": True
}

#data = [student1, student2]
#print(json.dumps(data, indent=4, sort_keys=True))
#with open("students.json", "w") as w:
#	json.dump(data, w, indent=4, sort_keys=True)
#data_json = json.dumps(data, indent=4, sort_keys=True)
#data_again = json.loads(data_json)
#print(sum(data_again[0]["scores"]))
with open("students.json", "r") as f:
	data_again = json.load(f)
	print(sum(data_again[1]["scores"]))
'''
'''
import csv
file_name = "users.csv"
users =[
	{"name": "Tom", "age": 45},
	{"name": "Alice", "age": 17},
	{"name": "John", "age": 23},
]
with open(file_name, "w", newline="") as file:
	# Создает объект writer, потом устанавливает заголовок с массива
	writer = csv.DictWriter(file, ["name", "age"])
	print(writer)
	writer.writeheader()
	print(writer)

	# Запись нескольких строк
	writer.writerows(users)

	user = {"name": "Anton", "age": 34}
	# запись одной строки
	writer.writerow(user)

with open(file_name, "r", newline="") as file:
	reader = csv.DictReader(file)
	print(reader)
	for row in reader:
		print(row["name"], "-", row['age'])
'''
'''
import json
classes = json.loads(input())
classes_dict = dict()
for instance in classes:
	classes_dict[instance["name"]] = set(instance["parents"])
def is_instance(parent, children):
	if parent in classes_dict[children] or parent == children:
		return True
	else:
		for i in classes_dict[children]:
			if i == []: 
				return False
			else:
				if is_instance(parent, i):
					return True
output = {}
for instance_parent in classes:
	count_children = 0
	for instance_children in classes:
		if is_instance(instance_parent["name"], instance_children["name"]):
			count_children += 1
	output[instance_parent["name"]] = str(count_children)
print(output.keys())
print(list(output.keys()).sort())
for i in list(output.keys()).sort():
	print(i, ":", output[i])
'''