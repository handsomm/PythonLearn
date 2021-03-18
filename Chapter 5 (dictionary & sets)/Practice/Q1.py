# Write a programm to create a dictionary of hindi words eith values as their engilesh translation. Provide user with an option to look it up.

myDict = {
    "pankha" : "Fan",
    "Dabba" : "Box",
    "vastu" : "Items", 
}

print("Options are ", myDict.keys())
a = input("Enter the hindi word\n")
# print("The meaning of your word is: ", myDict[a])
print("The meaning of your word is: ", myDict.get(a))
