# Write a programm to find greater of four numbers entered by the user

n1 = int(input("Enter the 1st Number: "))
n2 = int(input("Enter the 2nd Number: "))
n3 = int(input("Enter the 3rd Number: "))
n4 = int(input("Enter the 4th Number: "))

if(n1 > n2):
    f1 = n1
else:
    f1 = n2

if(n3 > n4):
    f2 = n3
else:
    f2 = n4

if(f1 > f2):
    print("The greater value is " + str(f1))
else:
    print("The greater value is " + str(f2))
