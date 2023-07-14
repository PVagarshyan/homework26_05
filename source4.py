import math

class InputError(Exception):
    pass
class SignError(Exception):
    pass

flag = True

while flag:
    try:
        a = eval(input("Year: "))
        if type(a) != int:
            raise InputError("Year can only be a whole point value!!")
        elif a < 0:
            raise SignError("Year cannot be negative!!")
        else:
            flag = False
    except NameError as err:
        print("Typing is incorrect")
    except InputError  as err:
        print(str(err))
    except SignError  as err:
        print(str(err))
    else:
        print("Thank you!!")


div4 = a//4 - 400 
div400 = a//400 - 400

if div4 <= 0:
    result = 0
elif div4 > 0 and div400 < 0:
    result = div4
else:
    result = div4 - div400
print(f"Between 1600 and {a} there are {result} number of leap years")

