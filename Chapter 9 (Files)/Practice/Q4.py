# A file contains a word "Donky" multiple times. You need to write a programm which replaces this word with ###### by updating the same file

with open("demo.txt") as f:
    content = f.read()

content = content.replace("donky", "$%^&@$$^#")

with open("demo.txt", 'w') as f:
    content = f.write(content)