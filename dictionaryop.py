data_list = [{'id': 1, 'name':'fahmi'}, {'id': 2, 'name':'shamsu'}, {'id': 3, 'name':'sana'},{'id': 4, 'name':'hadi'},{'id':5,'name':'huda'}]
subtitle = []
#add elements to a list from dictionary by name
for value in data_list:
   subtitle.append(value['name'])
print(subtitle)

#added elements are deleted from the list
for value in data_list:
    subtitle.remove(value['name'])
print(subtitle)

#deletion by particular id
for value in data_list:
    print("value :",value)
    if value["id"] == 3:
        data_list.remove(value)
print(data_list)

#updation by a particular id
for value in data_list:
    if value["id"] == 2:
        value["name"] = "fag"
print(data_list)