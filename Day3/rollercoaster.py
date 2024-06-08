print("Welcome to Python Rollercoaster!")
str_height = input("What is your height in cm?\n") #returns string
height = int(str_height)
bill = 0

if height > 120:
    str_age = input("How old are you?\n")
    age = int(str_age)
 
    if age < 12:
        bill += 5
    elif age >= 12 and age <=18:
        bill += 7
    elif age > 18 and age < 45:
        bill += 12
    elif age >= 45 and age <= 55:
        bill += 0
    
    want_photos = input("Do you want your photos after the ride? Please enter 'Y or 'N'.\n")

    if want_photos == "Y":
        if age < 45: 
            bill += 3
        elif age >= 45:
            bill += 0
    elif want_photos == "N":
        bill += 0

    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you are not tall enough to ride the Python Rollercoaster.")