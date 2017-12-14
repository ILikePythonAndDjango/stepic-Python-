# -*- coding: utf-8 -*-
# lesson 3.6: API
'''
import requests

# consts
city = input("Please, input city: ")
api_key = "11c0d3dc6093f7442898ee49d2430d20"
api_url = "http://api.openweathermap.org/data/2.5/weather?"

params = {
	"q": city,
	"appid": api_key,
	"units": "metric",
}

res = requests.get(api_url, params=params)
#print(res.status_code)
#print(res.headers["Content-Type"])
#for field in res.json().keys():
#	print(field, "=", res.json()[field])
data = res.json()
temp = data["main"]["temp"]
print("Current temperature in {} is {}".format(city, temp))
'''
'''
import requests, sys
with open("dataset_24476_3.txt") as file:
	for line in file.readlines():
		response = requests.get("http://numbersapi.com/{}/math?json=true".format(line.strip()))
		if response.json()["found"]: print("Interesting")
		else: print("Boring")
''' 
"""Задача со stepik.org

Нужно по индефикатору получить информацию о имени художника и годе рождения.
Вывести имена художников в порядке возврастания года. В случае если художников
одинаковый год рождения, то нужно вывести их имена в лексигарфическом порядке.

Для нужно использовать сервис artsy.net. На нем нужно зарегистрироваться и
создать свое приложение. После чего сервис выдаст константы: Client Id and Client Secret.
Затем нужно получить доступ к токену API. После нужно получить информацию с сервиса в json
формате. Input для программы будет являтся файл, который содержит все индейикаторы художников.
Output для программы это простоый вывод в cmd(Windows) имен художников, отсортерованной по их
дате рождения и именам.
"""
import requests
client_id = "bdd98e4cebaf6669b069"
client_secret = "981f60b3fc2fb4a62abc5770f294ce7b"
response = requests.post("https://api.artsy.net/api/tokens/xapp_token", data={"client_id":client_id,"client_secret":client_secret})
response.enconding = "utf-8"
json = response.json()
token = json["token"]
artists = dict()
with open("E:\\download\\dataset_24476_4.txt") as file:
	for line in file.readlines():
		line = line.rstrip()
		response = requests.get("https://api.artsy.net/api/artists/{}".format(line), headers={"X-Xapp-Token":token})
		response.enconding = "utf-8"
		if response.status_code == 200:
			artists[response.json()["sortable_name"]] = response.json()["birthday"]
artists_list = sorted(artists.items(), key=lambda x: (x[1], x[0]))
for artist in artists_list:
	print(artist[0])
with open("answer.txt", "w") as file:
	for artist in artists_list:
		file.write(artist[0] + "\n")