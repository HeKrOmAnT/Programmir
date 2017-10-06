buys = ["Хлеб","Молоко","Телевизор","Шуруповёрт 'Bosh'"]
print(buys)
print(buys[1])
print(buys[-1])
print(buys[1:])
buys.append("Маска человека-паука")
print(buys)
buys.insert(2,"Маска халка")
print(buys)
another_buys = ["Холодильник","Плойка"]
# buys.append(another_buys)
buys.extend(another_buys)

print(buys)
del buys[1]
print(buys)
buys.remove("Телевизор")
print(buys)
print(buys.pop(2))

print(buys)
# buys2 =buys
buys2=buys[:]
del buys[2]
print(buys)
print(buys2)