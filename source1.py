class InputError(Exception):
    pass
flag = True

while flag:
    try:
        input_int_kilogram = eval(input("Weight in kilograms: "))
        if(type(input_int_kilogram) == int):
            flag = False
        else:
            raise InputError("Sorry, but the value you entered does not match the requested one!!")
    except NameError as err:
        print("Sorry, but the value you entered does not match the requested one")
        flag = True
    except InputError as err:
        print(str(err))
        flag = True
    else:
        print("Thank you!!")
weight_in_pounds = input_int_kilogram * 2.2

print("weight in pounds ->", weight_in_pounds)



