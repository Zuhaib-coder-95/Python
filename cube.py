def cube(number):
    return number*number*number

def by_three(number):

    if number % 3 == 0:
        print('The number is divisible by 3')
        return cube(number)
    else:
        print('The number is not divisible by 3')
        return False
    

print(by_three(9))
print(by_three(4))