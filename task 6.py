#SET

'''a={1,2,3,4,5,6,7,3,1,6}
print(a)
a.add(60)
print(a)
a.remove(4)
print(a)
print(len(a))
if 3 in a:
  print('Yes')
else:
  print('No')
for i in a:
  print(i)
print(max(a))
print(min(a))
print(sum(a))

#Set Operation

a={1,2,3,4}
b={3,4,5,6}
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
e=a.difference(b)
print(e)
f=a.symmetric_difference(b)
print(f)
print(a.issubset(b))
print(a.isdisjoint(b))
g=[1,2,3,4,5,6,7,8,9,2,4,6,8]
con=set(g)
print(con)

#DICTIONARY

a={'Name':'Vimal','Age': 29,'City':'Salem'}
print(a)
print(a['Name'])
a['Course']='Python'
print(a)
a['Age']=30
del a['City']
print(a)
print(len(a))
if 'Name' in a:
  print('Yes')
else:
  print('No')
print(a.keys())
print(a.values())
for key, value in a.items():
  print(key, ':' ,value)

a={'Vimal': 414, 'Arun': 350, 'Shanmugam': 452, 'Barath': 385, 'Saran': 465}
print("Students:", a)
highest = max(a, key=a.get)
print("Highest mark:", highest, a[highest])
lowest = min(a, key=a.get)
print("Lowest mark:", lowest, a[lowest])
total = sum(a.values())
print("Total marks:", total)
average = total / len(a)
print("Average mark:", average)
count = sum(1 for mark in a.values() if mark > 400)
print("Students scoring above 400:", count)
name='Vimal'
if name in a:
    print(name, "scored", a[name])
else:
    print(name, "not found")
a['Vimal'] = 500
print("After :", a)
del a['Arun']
print("After :", a)

products = {"Laptop": 65000, "Mouse": 450, "Keyboard": 1200, "Headphones": 800, "Pen Drive": 400, "Monitor": 12000}
for product, price in products.items():
    if price > 500:
        print(product, "₹", price)'''
