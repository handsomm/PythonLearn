# An empty set is created using the below syntax
a = {2, 5, 4, 3, 6}
b = set()
print(type(b))

# Set methods
# Adding values in a set
b.add(1)
b.add(2)
b.add(3)
b.add(5)
b.add((4, 5, 6))
# b.add({4:5})  # Can't add dictionary or list
print(b)

print(len(b)) # Print the length of the set

b.remove(5) # Remove the value 5
print(b)

print(b.pop()) # Remove a random value
print(b)

print(b.clear()) # Empty the hole set

c = {1, 8, 9, 7, 6}
print(c.union(a))
print(c.intersection(a))