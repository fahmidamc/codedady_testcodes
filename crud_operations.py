def listop():
    print("list creation")
    print("=================")
    List = []
    print("blank list")
    print(List)
    List = ["happy", "pleasure", "1","fahmi","24","45"]

    print("\n display List Items: ")
    print("=================")
    print(List[0])
    print(List[1])
    print(List[2])

    print("\nAdding elements")
    print("=================")
    List.append("hi")
    List.append("i am")
    List.append("new one")
    print("\nList after Addition of Three elements: ")
    print(List)

    print("update list")
    print("=============")
    print("Value available at index 2")
    print(List[0])
    List[0] ="update"
    print("New value available at index 2")
    print(List[0])
    print(List)

    print("deletion of element")
    print("=====================")

    print("1.deletion by pop")
    print("------------------")
    print("before deletion")
    print(List)
    List.pop(0)
    print("After deletion")
    print(List)

    print("2.deletion by remove")
    print("----------------------")
    print("before deletion")
    print(List)
    List.remove("i am")
    print("after deletion")
    print(List)

    print("3.deletion by del")
    print("----------------------")
    print("before deletion")
    print(List)
    del List[6]
    print("after deletion")
    print(List)
def tupleop():
    print("tuple creation")
    print("=================")
    my_tuple = ()
    print("empty tuple")
    print(my_tuple)
    my_tuple = (1, "Hello", 3.4,2,5)
    print(my_tuple)
    print("display by index")
    print("=================")
    print(my_tuple[0])
    print(my_tuple[1])
    print(my_tuple[2])
    print(my_tuple[3])
    print("delete tuple")
    print(my_tuple)
    del my_tuple
def setop():
    print("set creation")
    print("=================")
    my_set = {1, 3}
    print(my_set)

    print("adding elements to set")
    print("========================")
    my_set.add(.5)
    print(my_set)

    print("update set")
    print("=================")
    my_set.update([2, 4])
    print(my_set)

    my_set.update([4, 5], {1, 6, 8})
    print(my_set)

    print("delete set element")
    print("===================")
    my_set.discard(4)
    print(my_set)

    my_set.remove(6)
    print(my_set)

    print("clear set")
    my_set.clear()
    print(my_set)
def dictop():
    print("dictionary creation")
    print("======================")
    my_dict = {1: 'apple', 2: 'ball', 'name': 'jack'}
    print(my_dict)
    print("display by key")
    print("=================")
    print(my_dict['name'])
    print(my_dict.get('name'))
    print("updating name")
    print("================")
    my_dict['name'] = 'fahmi'
    print(my_dict)
    print("deleting a key")
    print("==================")
    print(my_dict.pop(2))
    print(my_dict)
    print("adding a new element")
    print("=====================")
    my_dict['color'] = 'red'
    print(my_dict)
while True:
    print("=================================================")
    print("select your operation.")
    print("1.list")
    print("2.tuple")
    print("3.set")
    print("4.Dictionary")
    print("5.exit")
    choice = input("enter the choice 1/2/3/4/5")
    if choice == '1':
        listop()
    elif choice == '2':
        tupleop()
    elif choice == '3':
        setop()
    elif choice == '4':
        dictop()
    elif choice == '5':
        print("exiting")
        break
    else:
        print("invalid")
