#A dictionary loop returns keys by default. 
# To print values, use .values(); 
# to print both, use .items().


# Print all keys in a dictionary

employee = {
    "name": "Priya",
    "department": "Data Engineering",
    "salary": 60000
}

for key in employee:
    print(key)

# Print all values

for value in employee.values():
    print(value)

# Print both keys and values
for key, value in employee.items():
    print(key, value)




scores = {
    "Ravi": 80,
    "Priya": 90,
    "Arjun": 75
}

for name in scores:
    print(name)



prices = {
    "laptop": 1000,
    "mouse": 200,
    "keyboard": 500
}

for item in prices:
    prices[item] = prices[item] + 100

print(prices)






for key, value in prices.items():
    if value > 500:
        print(key, value)