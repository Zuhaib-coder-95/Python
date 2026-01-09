print("Select your ride: ")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if choice == 1 :
    print("what type of bike? ")
    print("1.Scooty\n")
    print("2.Scooter\n")
    
    choice2=int(input("Enter you choice2: ")) 

    if choice2==1:  
        print("you have selected scooty")
    else:
        print("you have selected scooter")

elif( choice == 2):
    print("What type of car?")
    print("1.SUV")
    print("2.Sedan")

    choice3= int(input("Enter your choice: "))
    if choice3==1: 
        print("You have selected SUV")
    else:
        print("You have selected Sedan")

else:
    print("Wrong Choice!")
