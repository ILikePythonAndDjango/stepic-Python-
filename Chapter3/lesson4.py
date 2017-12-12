# -*- coding: utf-8 -*-
# lesson 3.4: Internet: http-querys, html-pages and requests

import requests

'''
res = requests.get("https://docs.python.org/3.5/_static/py.png")
print(res)
print(res.status_code)
print(res.headers["Content-Type"])
for i in res.headers.keys():
	print(i, res.headers[i])
print(res.content)

with open("python.png", "wb") as f:
	f.write(res.content)

#print(res.text)
'''
'''
res = requests.get("https://yandex.ru/search/", 
					params={
						"text":"Stepic",
						"test":"test1",
						"name":"Name With Spaces",
						"list":["test1", "test2"]})
print(res.status_code)
print(res.headers["Content-Type"])
print(res.url)
print(len(res.text))
'''

"""
Задача на проверку ссылок страницы.
На вход программы подается два url. Первый - это страница, которую нужно распасрсить.
Второй - это страница, которую нужно проверить.
Затем на output выводиться Yes, если все окей, и No, если все плохо.
Но нужно понимать, что из одного документа может не быть прямого пути.
Значит нужно через рекурсивную функцию проверить нахождение страницы по всем ссылкам данной страницы,
если же ее не нашлось, то нужно искать в тех страницах, которые имеют ссылки на данной странице. Но
эти ссылки могут повторяться. Значит нужно создать список,
элементы которого будут означать уже использованные ссылки.
Для этого нужно создать функци, которая будет принимать два параметра, и являтся булевым флагом.
Каждая страница -- это html. Тег гиперссылки выглядет вот так: <a href="https://domen.location/varibale">some_text</a>
Чтобы найти этот тег нужно испльзовать регулярные выражения. Для этого нужно использовать группы
"""
'''
import requests, re

def isreference(url1, url2):
	res = requests.get(url1)
	lst = list()
	lst1 = list()
	lst1.extend(lst)
	if res.status_code == 200:
		for i in re.findall(r"<a.*href=\"(.+)\".*>", res.text):
			lst.append(i)
		for i in lst:
			res = requests.get(i)
			lst1.extend(re.findall(r"<a.*href=\"(.+)\".*>", res.text))
		if url2 in lst1: return True
		else: return False
	else:
		return False

url1 = input()
url2 = input()

if isreference(url1, url2):
	print("Yes")
else:
	print("No")
'''
'''
import re
import requests

start_url = input()
end_url = input()

found = False

link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

resp = requests.get(start_url).text
for url in link_pattern.findall(resp):
    cur_resp = requests.get(url).text
    if end_url in link_pattern.findall(cur_resp):
        found = True
        break

print("Yes" if found else "No")
''' 
'''
Следующая задача:
На вход подаются тег ссылки. И нужно вывести все сайты.
'''
import re, sys
pattern_href = r'<a.+href[ ]*=[ ]*"(.+)".*>'
pattern_domenpage = r"((.+)\.(ru|org|com|net))"
domen_list = list()
try:
	for line in sys.stdin:
		line = line.rstrip()
		href = re.findall(pattern_href, line)
		if href and re.findall(pattern_domenpage, href[0]):
			domen_list.append(re.findall(pattern_domenpage, href[0])[0][0])
except KeyboardInterrupt:
		pass
for domen in domen_list: print(domen)
