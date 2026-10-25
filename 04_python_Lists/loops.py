numbers = [10, 20, 30, 40]

result = [number * 3 for number in numbers]

print(result)




numbers = [10, 20, 30, 40, 50]

result = [number for number in numbers if number > 20]

print(result)



sales = [100, 250, 80, 400, 150]
result = [amount for amount in sales if amount > 200]

print(result)



sales = [100, 250, 80, 400, 150]

result = ["High" if amount >= 200 else "Low" for amount in sales]

print(result)



numbers = [10, 15, 20, 25, 30]
result_1 = [number for number in numbers  if number > 15 ]
result_2 = ["even" if number % 2 == 0 else "odd" for number in numbers]
print(result_1)
print(result_2)