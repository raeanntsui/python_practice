def prime_checker(number):
    is_a_prime_number = True
    for i in range(1, number + 1):
        if number % i == 0:
            is_a_prime_number = False
    if is_a_prime_number:
        print("This is a prime number.")
    else:
        print("This is not a prime number!")

n = int(input("Check this number\n"))
prime_checker(number=n)