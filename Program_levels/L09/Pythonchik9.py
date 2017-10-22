# # def sos():
# # 	x = 5
# # 	y = x * x
# # sos()

# def sos(x):
# 	y = x * x / (x + x)
# 	return y
# sos(5)
# print(sos(5))

# def my_sum(y, z):
# 	# x = y + z
# 	return x
# print(my_sum(2, 6))

# def my_div(x, z):
# 	return x / z

# print(my_div(2, 10))

# def lucky_list(judge, victim, sherif, executioner):
# 	print(sherif + " Требую екзекуции и справедливости ")
# 	print(judge + " Благославляю на казнь! ")
# 	print(executioner + " Отправил " + victim + " на курсы по Паскалю " )
# lucky_list(victim = "Сулейманчика", executioner = "Гаджи", sherif = "Гаминид", judge = "Бабушка Аня")
# import random
# def freud(victim, is_mad):
# 	#is_mad == random.randint(1,3)
# 	if is_mad == 1:
# 		print("Фрейд, радостно потирает руки, достаёт сигару и тушит её об " + victim)
# 	elif is_mad == 2:
# 		print("Фрейд с грустью зажигает её об " + victim)
# 	else:
# 		print("Вы и есть Фрейд")

# mad = random.randint(1,3)
# freud("Саида",mad)

# def reptiliod_list(*args, **kwags):
# 	print("Остерегайтесm их: ", args)
# 	print("Стрелять без предупреждения по: ", kwags)

# reptiliod_list("Сулейманчек", "Султанмурад", "Гаджи","Эльдар","Вера Андреевян", jidomasson = "Саид")