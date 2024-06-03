print("Welcome to the tip calculator!")
total = input("What was the total bill?\n")
tip = input("How much tip would you like to give? 10%, 12%, or 15%?\n")
people = input("How many peope are splitting this bill?\n")

result = (float(total) * (int(tip) / 100)) / int(people)

print("Each person should pay $" + str(result))