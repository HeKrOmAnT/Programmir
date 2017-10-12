import random
player1 = {"счёт": 1000}
player2 = {"счёт": 1000}
player1["имя"] = input("Введите имя первого игрока:")
player2["имя"] = input("Введите имя второго игрока:")

while True:
	player1["ставка"] = int(input("Введите ставку:"))
	player2["ставка"] = int(input("Введите ставку:"))

	player1["бросок"] = random.randint(2,12)
	player2["бросок"] = random.randint(2,12)


	if player1["бросок"] > player2["бросок"]:
		print(player1["имя"], "выиграл ставку")
		player1["счёт"] += player2["ставка"]
		player2["счёт"] -= player2["ставка"]
	elif player1["бросок"] < player2["бросок"]:
		print(player2["имя"], "выиграл ставку")
		player2["счёт"] += player1["ставка"]
		player1["счёт"] -= player1["ставка"]
	else:
		print("ничья")

		#(player1["счёт"])
	print(player1["счёт"])
	#(player2["счёт"])
	print(player2["счёт"])

	#(player1["бросок"])
	#print(player1["бросок"])
	#(player2["бросок"])
	#print(player2["бросок"])

	# if player1["ставка"] > player2["ставка"]:
	# 	print(player2["ставка"])
	# elif player2["ставка"] > player1["ставка"]:
	# 	print(player1["ставка"])

	if player2["счёт"] <= 0:
		print(player1["имя"], "победил")
		break
	elif player1["счёт"] <= 0:
		print(player2["имя"],"победил")
		break
	
	# if player1["ставка"] > player1["счёт"]:
	# 	player1["ставка"] = player1["счёт"]
	# elif player2["ставка"] > player2["счёт"]:
	# 	player2["ставка"] = player2["счёт"]