
#shallow copy vs deep copy



import copy

a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)

b[0][0] = 999

print(a)
print(b)





a = [[10, 20], [30, 40]]
b = a.copy()

b[0][0] = 999

print(a)
print(b)



a = [10, 20, 30]
b = a

b[1] = 999

print(a)





sales = [100, 200, 300]

backup = sales.copy()

backup[0] = 999
sales.append(400)

print(sales)
print(backup)



a = [10, 20, 30]

b = a.copy()

b.append(40)

print("a =", a)
print("b =", b)