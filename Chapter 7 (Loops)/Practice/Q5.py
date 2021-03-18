# Write a programm to find the sum of first n natural number using while loop.

n = int(input("Enter a number: "))

if n < 0:
    print("Enter a positive number")
else:
    sum = 0
    i = 0
    while i <= n:
        sum += i
        i += 1
    print(f"The sum of {n} numbers is {sum}")

    