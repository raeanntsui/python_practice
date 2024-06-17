fizzbuzz_number = 20

stopping_point = fizzbuzz_number + 1

for number in range(1, stopping_point):
    # print(f"The current # = {number}")
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)