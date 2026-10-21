count = 1

while count <=5:
    print(count)
    count += 1


count = 5

while count >=1:
    print(count)
    count -= 1

count = 2

while count %2 == 0 :
    print(count)
    count += 1


records = 1
while records <=5:
    print("Processing record ", records)
    records += 1


number = 1
total =0
while number <=5:
    print(number)
    total += number
    number += 1
    


records = 1
while records <=5:

    if records == 4:
        print("bad record found")
        break

    print("Processing record ", records)
    records += 1  



numbers = 1
while numbers <=5:
    print(numbers)
    numbers += 1


number = 1
total = 0

while number <=5:
    total += number
    print(number)
    number += 1


print(total)

for numbers in range(1, 10):
    if numbers == 5:
        break
    print(numbers)


numbers = [10, 20, 30, 40, 50]

for numbers in range(5):
    if numbers == range(3):
        break 

    print(numbers)