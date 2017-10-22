import random

def show_health(player):
	print("Количество жизней игрока: ", player["имя"], player["HP"])
def creat_player():
	player = {"HP": 5000, "Урон": 300}
	player["имя"] = input("Введите свое имя, боец: ")
	choose = input("1 - увеличить HP на 2000, 2 - увеличить урон на 135 ")
	if choose == "1":
		player["HP"] += 2000
	else:
		player["Урон"] += 135
	return player

def show_health(player):
	print("Количество жизней игрока: ", player["HP"])

def attack(attacker, victium):
	damage = random.randint(attacker["Урон"] - 100, attacker["Урон"] + 100)
	print(attacker["имя"], "нанёс", damage, "единиц урона")
	victium["HP"] -= damage


player1 = creat_player()
player2 = creat_player()
#player2 = creat_player()
while True:
	attack(player1,player2)
	attack(player2,player1)

	show_health(player1)
	show_health(player2)

	input()

	if player1["HP"] <= 0:
		print(player2["имя"], "выиграл!!!")
		break
	elif player2["HP"] <= 0:
		print(player1["имя"], "выиграл!!!")
		break
	elif player2["HP"] <= 0 and player2["HP"] <= 0:
		print("НИЧЬЯ")
		break