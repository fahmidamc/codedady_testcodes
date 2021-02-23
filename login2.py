cpas = "admin"
user = input("enter username")
pas = input("enter password")

while True:
    if pas == cpas:
        print("login success")
    elif pas != cpas:
        print("login failed")

    else:
        print("invalid choices")
    break

