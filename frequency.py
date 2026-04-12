test_dict = {
    'Codingal' : 2,
    'is' : 2,
    'best' : 2,
    'for' : 2,
    'Coding' : 1
}

value = 2
result = 0

for key in test_dict:
    if test_dict[key] == value:
        result = result + 1

print("Frequency of 2 is : " + str(result))