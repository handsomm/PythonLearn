# Print multiplication table in reverse order

num = int(input("Enter a number: "))
for column in range(10,0,-1):
    print(f"{num} X {column} = {num*column}",end="\n")
