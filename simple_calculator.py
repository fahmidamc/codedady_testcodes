#create a simple calculator
#addition
#substraction
#multiplication
#division

#refer : try, except

#code should not break unless the user decide

def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    return x / y



while True:
    print("=================================================")
    print("select your operation.")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.exit")
    choice = input("enter the choice 1/2/3/4/5")
    try:
        if choice in ('1','2','3','4') :
            a = float(input("enter the first number"))
            b = float(input("enter the second number"))
        if choice == '1':
            print(a,"+",b,"=",addition(a,b))
        elif choice == '2':
            print(a,"-",b,"=",subtraction(a,b))
        elif choice == '3' :
            print(a,"*",b,"=",multiplication(a,b))
        elif choice == '4' :
            print(a,"/",b,"=",division(a,b))
        elif choice == '5':
            print("program exiting")
            break

        else:
            print("invalid choice")

    except Exception as e:
        print(e)
    #
    # except ValueError:
    #     print("invalid",'value error!')
    #
    #
    # except ZeroDivisionError:
    #     print(a, '/', b, ':', 'Division by zero!')