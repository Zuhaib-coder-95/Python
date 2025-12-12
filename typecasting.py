name = "Samuel"
age = 15
is_student = True
weight = 38.5
yearofbirth = "2000"

print("Before Typecasting:")
print("Type of yearofbirth is:" , type(yearofbirth))
print()

yearofbirth = int(yearofbirth)

print("After typecasting:")
print("Type of yearofbirth is:" , type(yearofbirth))

print("My name is", name)
print("Data type of isstudent:", type(is_student))