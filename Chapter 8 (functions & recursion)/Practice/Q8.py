# Write a python programm to print multiplication table of a given number

def mul_table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")
    
n = int(input("Enter a number: "))
mul_table(n)