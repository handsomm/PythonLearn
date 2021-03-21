# Writw a function to print first n lines of the following partten
#  * * *
#  * *
#  *

def partten(n):
    for i in range(n):
        print("*" * (n-i))

n = int(input("Enter a number: "))
partten(n)