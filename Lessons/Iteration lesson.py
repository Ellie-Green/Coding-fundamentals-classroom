# While loop
counter = 0

while counter < 5:
    name = input("Enter a name: ")
    print(name + " is awesome.")
    counter += 1

# For loop
for _ in range(5):
    name = input("Enter a name: ")
    print(name + " is awesome.")

# List comprehension + for loop for printing 
names = [input("Enter a name: ") for name in range(5)]
for name in names:
    print(f"{name} is awesome.")

#List comprehension one line
[print(f"{name} is awesome.") for name in [input("Enter a name: ") for x in range(5)]]