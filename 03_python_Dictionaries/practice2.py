product = {
      "name":  "Saree",
      "price":1000,
      "quantity" :5
      }

print(product["name"])

product["category"] = "Fashon"
product["price"]=750

print(product.get("city", "unknown"))
stock = product.setdefault("stock",10)
print(stock)


product.update({"price" : 50000,
               "supplier": "amazon"})
print(product)


#for product in product:
 #   if "price" > 10000:


#salary = product["salary"] *1.10

#/updated_salary ={
#     name : salary *1.10
#    for name ,salary in product.items()}
