# Write a programm to fine a given number is prime or not.

num = int(input("Enter the number: "))
prime = True
for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is prime.")
else:
    print("This is not a prime number.")
