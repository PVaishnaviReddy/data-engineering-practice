a = [10, 20]
a.append(30)
print(a)

a= [10, 20]
a.append([30, 40])
print(a)



a= [10, 20]
a.insert(2, 30)
print(a)


a= [10, 20]
a.extend([30, 40])
print(a)




sales = [[10, 20],
         [30, 40],
         [50,60]
        ]

sales[0][1]= 50
print(sales)

#list comprehension

sales = [10, 20, 50]

new_sales = (sale*2 for sale in sales )

print(new_sales)
print(sales)

#2
sales = [10, 20, 50]

new_sales = ("Good" if sales in sales >30 else "bad"for sale in sales)

print(new_sales)
print(sales)



#3 copy vs shallowcopy 

a=[10,20]
b=a.copy()
b.append(30)
print("a  = ", a )
print("b  = ", b )





a=[[10,20],[30,40]]
b= a.copy()
b[0][1]= 99
print("a  = ", a )
print("b  = ", b )




import copy
a=[[10,20],[30,40]]
b= copy.deepcopy(a)
b[0][1]= 99
print("a  = ", a )
print("b  = ", b )