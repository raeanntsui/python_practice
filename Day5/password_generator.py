import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letter_count = (input("How many alphabet letters would you like in your password?\n"))
symbol_count = input("How many symbols would you like in your password?\n")
number_count = input("How many numbers would you like in your password?\n")



int_letter_count = int(letter_count)
int_symbol_count = int(symbol_count)
int_number_count = int(number_count)

password_length = int_letter_count + int_symbol_count + int_number_count

password_letters = []
password_symbols = []
password_numbers = []

for chosen_letter in range(1, int_letter_count + 1):
    if len(password_letters) == int_letter_count:
        break
    else:
        password_letters.append(random.choice(letters))

for chosen_symbol in range(1, int_symbol_count + 1):
    if (len(password_symbols) == int_symbol_count):
        break
    else: password_symbols.append(random.choice(symbols))

for chosen_number in range(1, int_number_count + 1):
    if (len(password_numbers) == int_number_count):
        break
    else: password_numbers.append(random.choice(numbers))

# new_password = "".join(password_letters) + "".join(password_symbols) + "".join(password_numbers)
new_password = "".join(password_letters + password_symbols + password_numbers)
print(f'New password is {new_password}')

# print("Here is a shuffled version of your password:")
test