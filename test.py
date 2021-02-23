
dictionary = [
    {"id":1,"name":"asd"},
    {"id":2,"name":"asda"},
    {"id":3,"name":"weqw"},
    {"id":4,"name":"vfdd"},
]
cart = []
flag=0
for x in dictionary:
    if 4== x["id"]:
        flag=1
        cart.append(x["name"])
    if flag==1:
        break

if flag==1:
    print("Item added")
else:
    print("Item not found")

if len(cart) > 0:
    print("order placed")

dict = {"name" : "John", "age" : 20}
a_list = []

dictcopy = dict.copy()
a_list.append(dictcopy)
print(a_list)

x = [2, 4, 7, 12, 3]
total = sum(x)
print(total)

for value in x:
    total += value
print(total)