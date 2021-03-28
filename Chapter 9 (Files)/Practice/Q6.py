# Write a programm to mine a log file and find out  whethir it contains "python". and also find line number.

content = True
i = 1
with open("log.txt") as f:
    while content:

        content = f.readline()

        if 'python' in content.lower():
            print(content)
            print(f"python is present on line number {i}")
        i += 1