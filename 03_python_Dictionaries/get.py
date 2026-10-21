# get() is a method, 
# so we use parentheses (). 
# It does not remove anything from the dictionary.

order = {
    "order_id": 101,
    "price": 500
}

print(order.get("quantity", 1))


customer = {
    "customer_id": 101,
    "name": "Ravi"
}

age = customer.get("age", 0)

print(age)


product = {
    "name": "Laptop",
    "price": 60000
}

print(product.get("quantity", 1))