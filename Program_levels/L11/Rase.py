import random


def ride(car):
	car["distance"] += car["speed"]
	car["fuel"] -= car["spend"]

def faster(car):
	car["speed"] += 2
	car["spend"] += 2

def nitro(car):
	car["distance"] += car["speed"]
	car["fuel"] -= car["spend"] * 3

def info(car):
	print("\n Тeкущее состояние:",
		"Топливо:" + str(car["fuel"]),
		"Скорость:" + str(car["speed"]),
		"Проехали:" + str(car["distance"]) + "/" + str(track))

def rase_step(car):
	choose = input("Твой ход," + car["name"] + "Что будем делать?")
	if choose == "1":
		ride(car)
	elif choose == "2":
		faster(car)
	else:
		nitro(car)
	rase_step(car1)
	rase_step(car2)
	rase_step(car3)

info(car)

input()

car1 = {
	"name": "Чайка",
	"speed": 5,
	"fuel": 25,
	"spend": 2,
	"nitro": 8,
	"distance": 0
}
car2 = {
	"name": "Нива",
	"speed": 3,
	"fuel": 35,
	"spend": 3,
	"nitro": 11,
	"distance": 0
}
car3 = {
	"name": "Шиха",
	"speed": 6,
	"fuel": 30,
	"spend": 5,
	"nitro": 10,
	"distance": 0
}

track = 40

if car["fuel"] <= 0:
	print(car["name"] + "ПРОИГРАЛ!")
elif car["fuel"] >= 1:
	continue

if car["distance"] == 40:
	print(car["name"] + "Выиграл!")
elif car["distance"] <= 39:
	continue