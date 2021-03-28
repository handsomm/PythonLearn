# Write a programm to make a copy of a text file "this.txt"

with open("this.txt") as f:
    content = f.read()

with open("copy2.txt", 'w') as f:
    f.write(content)
