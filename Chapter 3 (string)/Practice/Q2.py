# Write a programm to fill in a letter template given below with name and date

letter = '''Dear <|NAME|>,
You are selectrd!

Date: <|DATE|>'''

name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)