# # guest = input("Введите список пришедших гостей")
# # print(guest)
# # list_of_guest = guest.split(",")
# # print(list_of_guest[0])

# # final_guest = " + ".join(list_of_guest)
# # print(final_guest + " = Ненависть на всегда!")

numbers = input("Введите числа")
numbers_list = numbers.split(" ")

print(numbers_list)

n = 0
for i in numbers_list:
	numbers_list[n] = int(i)
	n += 1

# print(numbers_list)
print(len(numbers_list))
# print(min(numbers_list))
# print(max(numbers_list))
# numbers2 = [20, 15, 21, 99]
# numbers3 = {5:"пять", 10:"десять", 15:"девять", 20:"нуль"}

# guess = int(input("Отгадай число: "))

# print(guess in numbers2)
# if guess in numbers2:
# 	print("Ты чёртов экстрасенс!!")
# else:
# 	print("Ты обложался, парень!")

# if guess in numbers3:
# 	print("Ура,словарь")

# numbers4 = (10, 14, 22)
# for i in numbers4:
# 	print(i)
# numbers5 = {5:"пять", 10:"десять", 15:"девять", 20:"нуль"}
# for i in numbers5.items():
# 	print(i)
# numbers = 10
# for numbers in range(0,10):
# for i in range(0,10,2):
# 	print(i)