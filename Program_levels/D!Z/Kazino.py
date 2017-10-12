import random
player = {"счёт": 1000}
player["имя"] = input("Введите имя игрока:")
while True:
	player["ставка"] = int(input("Введите ставку:"))
	player["ставка"] < player["счёт"] 
	player["супер_код"] = input("Введите супер_код от 1 до 36 :")
	player["бросок"] = random.randint(1,37)
	if player["бросок"] == random.randint(1,37):
		player["счёт"] += player["ставка"]*36
		print(player["счёт"] + player["ставка"])
		print("Поздравляем ваша ставка Х36!!!!!!")
	else:
		player["счёт"] -= player["ставка"]
		print("Вы проиграли!")
		print(player["счёт"])
	if player["счёт"] < 0:
		print("Берите кредит или убирайтесь вон")
		break
	else:
		continue 
	if player["счёт"] == 0:
		print("Увы, у Вас закончились деньги.Приходите ещё!")
		break
	else:
		continue