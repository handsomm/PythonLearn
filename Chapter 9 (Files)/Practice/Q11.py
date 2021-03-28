# Write a programm to rename a file to "rename_by_python.txt"
import os
oldname = "copy2.txt"
newname = "rename_by_python.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, 'w') as f:
    f.write(content)

os.remove(oldname)