# Write a programm to read the text from a given file 'poems.txt' and findout wheather it combines the word 'twinkle'.

f = open('./poem.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()