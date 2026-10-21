# Task             Syntax

#Read a value              order["price"]
#Update a value            order["price"] = 600
#Calculate using values    order["price"] * order["quantity"]


order = { 
        "order_id" : 101,
        "customer" : "ravi",
        "price" : 500,
        "quantity" : 2
        }

order["city"] = "siddipet"
order["price"]= 600
total_amount = order["price"] * order["quantity"]
print(order)
print(order["customer"])
print(total_amount)
print(order.get("discount",0))



order = { 
        "order_id" : 102,
        "customer" : "priya",
        "price" : 750,
        "quantity" : 3,
        "status" : "pending"
        }
print(order["order_id"])
order["status"] = "completed"
order["city"] = "Hyderabad"
total_amount = order["price"] * order ["quantity"]

print(order.get("discount" , 0))


print(total_amount)


print(order)

for key in order:
    print(key)


# Filter orders by status
orders = {
    "order1": {"price": 500, "status": "completed"},
    "order2": {"price": 800, "status": "pending"},
    "order3": {"price": 300, "status": "completed"}
}

for order in orders:
    if orders[order]["status"] == "completed":
         print(order,orders[order]["price"])





employees = {
    "emp1": {"name": "Ravi", "salary": 30000},
    "emp2": {"name": "Priya", "salary": 50000},
    "emp3": {"name": "Arjun", "salary": 25000},
    "emp4": {"name": "Sneha", "salary": 60000}
}

for employee in employees :
    if employees[employee]["salary"] > 30000:
        print(employees[employee]["name"], employees[employee]["salary"])





products = {
    "product1": {"name": "Laptop", "price": 50000},
    "product2": {"name": "Mouse", "price": 800},
    "product3": {"name": "Keyboard"}
}

for product in products:
    name = products[product].get("name")
    price = products[product].get("price", 0)
    if products("name") >1000:
        print(products) 
    print(name, price)