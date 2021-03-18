# Writ a programm to find wheather a given username contains less than 10 characters or not

user = input("Enter username:\n")

if(len(user) < 10):
    print("Length of the username is less than 10")
else:
    print("All set")
