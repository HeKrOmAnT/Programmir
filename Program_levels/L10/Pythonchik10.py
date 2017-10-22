import random 
# import Factorial
# from math import sqrt, cos
# from cmath import sqrt as complex_sqrt

my_list = ["1С","Google","Telegram","Yandex","Rambler"]
i=1
while i<=4:
	x = random.choice(my_list)
	print(x, "уничтожен")
	my_list.remove(x)
	i+=1
print("кек")
# print(sqrt(4))
# print(cos(8))
# print(complex_sqrt(-1))

# print(Factorial.lavash_factorial(-5))