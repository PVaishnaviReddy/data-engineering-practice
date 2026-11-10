record = ("ORD101", "Laptop", 2)

order_id, product, quantity = record

if quantity > 1:
    print(f"{product}: bulk order")



sales = (100, 200, 300)

for amount in sales:
    print(amount)


transactions = (500, 1200, 800, 1500)

total = 0

for amount in transactions:
    total = total + amount

print(total)



transactions = (500, 1200, 800, 1500)

print(sum(transactions))