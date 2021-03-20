# Write a programm using function to find greater of three number

def greater(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3

m = greater(5, 8, 22)

print("The greater number is " + str(m))