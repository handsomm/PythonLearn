myDict = {
    "first": "Hello Shibu",
    "shibu": "A Programmer",
    "marks": [1, 2, 3, 4, 5],
    "anotharDict": {
        'cbu': 'Coder'
    }
}

# Dictionary Methods
print(list(myDict.keys()))  # prints the keys of the dictonary
print(list(myDict.values()))  # prints the values thr dictionary
# prints the (key, value) for all contents of the dictionary
print(list(myDict.items()))
print(myDict)
updateDict = {
    "lovis": "friends",
    "chandan": "friend"
}
# Update the dictionary by adding key-value pairs from updateDictcle
myDict.update(updateDict)
print(myDict)

print(myDict.get("shibu1"))
# print(myDict["shibu1"])  # Throw an error
