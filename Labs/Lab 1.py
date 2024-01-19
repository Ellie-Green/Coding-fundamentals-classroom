# Part 1 
# Display text to the terminal. 
print('Hello world!')

# Part 2
# Display a message using variables 
username = 'Bob'
age = 32 
print(f'{username} is {age} years old.') 

# Part 3
# Get a user input and display a message. 
username = input('Please enter your name: ') # Asks the user for an input
age = int(input('Please enter your age: '))  # Asks the user for an input as an int
print(username + " is " + str(age) + " years old.") # Concatenation to add variables to the output message. # Casting is used to convert age to a string

# Part 4
# Take inputs from the user, perform calculations and cast the inputs into a string 
length = int(input('Enter the length of the rectangle: ')) # Asks for the user to input two integers
width = int(input('Enter the width of the rectangle: '))
perimeter = 2* (length + width)    # Calculates the perimeter by adding the length and width together then * by 2. (BODMAS)
area = length * width              # Calculates the area by * length and width together 
print(f'The perimeter of the rectangle is {perimeter}.') # Formats the output message to include the input in the correct form
print(f'The area of the rectangle is {area}.')

