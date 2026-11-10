daily_sales = [
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
]
for day in daily_sales:
    for sale in day:
        print(sale)



departments = [
    [10, 20],
    [30, 40]
]

for department in departments:
    for employee in department:
        print(employee * 2)





daily_sales = [
    [100, 600, 300],
    [800, 200, 900]
]
for day in daily_sales:
    for sale in day:
        if sale > 500:
            print(sale)



#Store the results in a new list
daily_sales = [
    [100, 600, 300],
    [800, 200, 900]
]

high_sales = []

for day in daily_sales:
    for sale in day:
        if sale > 500:
            high_sales.append(sale)

print(high_sales)




sales = [1200, 1600, 1800]
high_sales = []

for sale in sales:
    if sale > 500:
        high_sales.append(sale * 2)
print(high_sales)



daily_sales = [
    [100, 600, 300],
    [800, 200, 900]
]
high_sales = []

for day in daily_sales:
    for sale in day:
        if sale > 500:
            high_sales.append(sale * 2)

print(high_sales)




daily_sales = [
    [100, 600],
    [300, 800]
]

result = [sale for day in daily_sales for sale in day if sale > 400]

print(result)