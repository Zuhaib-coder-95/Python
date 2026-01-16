number= int(input("Enter a Number whose sum you want to find:"))

sum = 0

for i in range(1, number + 1):
    sum = sum + i

print("\nSum=", sum)