class InputError(Exception):
    pass

flag = True

while flag:
    try:
        a = eval(input("a: "))
        b = eval(input("b: "))
        if a + b == 0:
            raise ZeroDivisionError("You are trying to divide a number by 0!!")
        elif type(a) != int or type(b) != int:
            raise InputError("Your writing is not digital data!!")
        else:
            flag = False
    except ZeroDivisionError as err:
        print(str(err))
        flag = True
    except InputError as err:
        print(str(err))
        flag = True
    except NameError as err:
        print("Your writing is not digital data!!")
        flag = True
    else:
        print("Thank you!!")
result = abs(a - b)/(a + b)

print("|a - b| / ( a + b ) =", result) 
