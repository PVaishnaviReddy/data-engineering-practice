# pop() — remove a specific key
# pop() also returns the value that was removed.

order = {
    "order_id": 101,
    "price": 500,
    "quantity": 2
}

removed_price = order.pop("price")

print(removed_price)
print(order)

# del — delete a specific key

order = {
    "order_id": 101,
    "price": 500,
    "quantity": 2
}

del order["price"]

print(order)

# clear() — remove everything

employee = {
    "name": "Priya",
    "age": 29,
    "city": "Siddipet"
}
employee.clear()

print(employee)


# Checking whether a key exists

order = {
    "order_id": 101,
    "price": 500
}

print("price" in order)
print("quantity" in order)


