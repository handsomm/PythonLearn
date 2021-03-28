# Write a programm to generate multiplication table from 2 to 20 and write it to the different files. Place three files in a folder for a 13 year old.

for i in range(2, 6):
    with open(f"tables/multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i*j}")
            if j!=10:
                f.write('\n')