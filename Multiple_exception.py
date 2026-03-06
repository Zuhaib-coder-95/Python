try: 
    num1, num2 = eval(input("Enter two numbers, seperated by a comma: "))
    result = num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by ) is ERROR!!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1,2")

except:
    print("Wrong input")

else:
    print("No Exceptions")

finally:
    print("This wil print no matter what")