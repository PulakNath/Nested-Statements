n = input("Do you have a medical cause? Y/N: ").strip().upper()
if n == "Y":
    print("You are allowed")
else:
    a = int(input("Enter your attendence: "))
    if a >= 75:
        print("Allowed")
    else:
        print("Not allowed")
Units = int(input("Enter the number of units you consumed: "))
if (Units <= 50):
    amount = Units * 2.60
    surcharge = 25
elif (Units <= 100):
    amount = 130 + (Units - 50) * 3.25
    surcharge = 35
elif (Units <= 200):
    amount = 130 + 162.5 + (Units - 100) * 5.26
    surcharge = 45
else:
    amount = 130 + 162.5 + 526 + (Units - 200) * 7.50
    surcharge = 55
total = amount + surcharge
print("Total amount = %.2f" % total)
print("Select your ride: ")
print("1.Bike")
print("2.Car")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("What type of bike?")
    print("1.Motorcycle\n")
    print("2.Scooter\n")
    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        print("You have selected Motorcycle")
    elif choice2 == 2:
        print("You have selected Scooter")
elif choice == 2:
    print("What type of car?")
    print("1.Convertible\n")
    print("2.SUV\n")
    choice3 = int(input("Enter your choice: "))
    if choice3 == 1:
        print("You have selected Convertible")
    elif choice3 == 2:
        print("You have selected SUV")
else:
    print("Invalid choice")
