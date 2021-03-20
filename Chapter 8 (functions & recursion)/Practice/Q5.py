# Writw a function to print first n lines of the following partten
#  * * *
#  * *
#  *

n = int(input("Enter a number: "))
for i in range(n):
    print("*" * (n-i))
