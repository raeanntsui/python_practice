def prime_checker(number):
    if number == 6:
     print("hello 6")
    elif number % number == 0 and number % 1 == number and number % 2 == 0:
        print("This is not a prime number.")
    else:
        print("This is a prime number.")

n = int(input("Check this number\n"))
prime_checker(number=n)