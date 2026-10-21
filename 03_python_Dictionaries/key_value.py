employee = {
    "name": "Arjun",
    "salary": 40000
}

print("salary" in employee)
print("age" in employee)











employee = {
    "name": "Priya",
    "department": "Data Engineering"
}

employee["salary"] = 50000

print(employee)



product = {
    "name": "Laptop",
    "price": 60000
}

print(product.get("quantity", 1))