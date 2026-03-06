try:
    number = int(input("Enter Number"))
    print("The number entered is", number)

except ValueError as ex1:
    print("The Exception:", ex1)

except NameError as ex2:
    print("The Exception:", ex2)
