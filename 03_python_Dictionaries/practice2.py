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
print(product)