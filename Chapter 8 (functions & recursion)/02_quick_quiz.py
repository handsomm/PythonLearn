# Write a programm to greet a user with "Good day" using function

def greet(name):
    print("Good Day " + name)

name = str(input("Enter your name: "))
greet(name.capitalize())