class Auto:
	def __init__(self, wheels, body):
		self.wheels = wheels
		self.body = body

	def drive(self):
		print("НЕ поеду!!")
tesla = Auto(2, True)
tesla.wheels += 2
print(tesla.wheels)
print(tesla.body)
tesla.drive()

oka = Auto(10, False)