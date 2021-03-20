# Write a programm using function to convert celcius to farenhite

def far(cel):
    return (cel*(9/5)) + 32

c = float(input("Enter Celcius value: "))
f = far(c)
print("Farenhite temperature is " + str(f))