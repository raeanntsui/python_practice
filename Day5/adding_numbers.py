target = int(input("Enter a number between 0 and 1000!\n")) 
stop_point = target + 1
print(f"Stop point: {stop_point}")
if target > 1000:
    print("Please only input a number between 0 and 1000.")
else:
    total = 0
    for number in range(stop_point):
        if number % 2 == 0:
            print(f'---------the current number is: {number}')
            total = number + total
            print(f'The current total is {total}.')
    print(total)