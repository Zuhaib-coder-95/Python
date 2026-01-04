height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))


BMI = weight / (height/100)**2

print("Your BMI is ",BMI)


if BMI <= 18.4:
    print("You are underweight.")

elif BMI <=24.9 and BMI > 18.4:
    print("You are healthy.")

elif BMI <=29.9 and BMI > 24.9:
    print("You are overweight.")

else:
    print("You are obese.")