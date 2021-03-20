# Write a recursive function to calculate the sum of first n numbers.

def totalSum(n):
    if n == 1:
        return 1
    return n + totalSum(n-1)

num = int(input("Enter a number: "))
total = totalSum(num)
print(total)