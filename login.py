class login:
    # def __init__(self,id,pas):
    #     self.id = "admin"
    #     self.pas = "admin"

    def check(self,id,pas):
        #print(self.id)
        #print(self.pas)
        if(id == "admin" and pas == "123"):
            print("     LOGIN SUCCESS!      ")
        else:
            print("   INCORRECT PASSWORD OR USERNAME!     ")

log = login()
print("         LOGIN PAGE          ")
print("_______________________________")
logi = input("Enter Login ID:")
passi = input("Enter password:")
log.check(logi,passi)


class login:
    def check(self, id, pas):
        if (id == loginid and pas == pswd):
            print("     LOGIN SUCCESS!      ")
            return 1
        else:
            print("  LOGIN FAILED !!   ")
            return 0


log = login()
print("         LOGIN PAGE          ")
print("_______________________________")
logi = input("Enter Login ID:")
passi = input("Enter password:")
val = log.check(logi, passi)
