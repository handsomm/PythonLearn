# Write a python programm to remove a given word from a string and stop it at the same time

def remove(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Soumya is a good boy    "
n = remove(this, "boy")
print(n)