print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza would you like to order? Please type either S, M, or L\n")

bill = 0

if (size == "S" or size == "s"):
    valid = True
    bill += 15
elif (size == "M" or size == "m"):
    valid = True
    bill += 20
elif (size == "L" or size == "l"):
    valid = True
    bill += 25
else:
    valid = False

if valid:
    topping = input("Would you like to add PEPPERONI to your pizza? Please type 'Y' for Yes or 'N' for No.\n")
    if topping == "y" or topping == "Y":
        if (size == "s" or size == "S"):
            bill += 2
        elif (size == "M" or size == "m" or size == "L" or size == "l"):
            bill += 3
    else:
        bill += 0

    cheese = input("Would you like to add CHEESE to your pizza? Please type 'Y' for Yes or 'N' for No.\n")
    if (cheese == "Y" or cheese == "y"):
        bill += 1
    else:
        bill += 0

    print(f"Your final bill is: ${bill}.")
else:
    print("Please be sure you are typing S, M, or L only! Restart.b")