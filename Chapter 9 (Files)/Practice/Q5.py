# Repeat programm 4 for a list of such word to be censored

words = ['donky', 'mote', 'kaudday']

with open("demo.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^&@$$^#")

    with open("demo.txt", 'w') as f:
        f.write(content)
