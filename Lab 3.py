# Task 1 

# Part 1 - squares 
x = 0
square = ()

while x <= 100:     # Uses a while loop to print out the square of every number from 1 to 100 
    square = x ** 2
    if square > 2000:   # Will break the loop if the square is greater than 2000
        break
    print(f"{x} squared = {square}")
    x += 1

# Part 2 - factorial 
num = int(input("Enter a number: "))        # Takes an input from the user
factorial = 1
n = 1

while n <= num:                             # A while loop will work out the factorial for the users value
    factorial = factorial * n               # Factorial - that number multiplied by all preceding numbers
    n = n + 1
print(f"The factorial of {num} = {factorial}")

# Part 3 - investment

initial_investment = int(input("Enter your starting amount: £"))    # Works out how many years it will take for an amount to reach a target value based off of the interest rate
target_value = int(input("What is your target value? £"))
interest_rate = int(input("What is the interest rate (in %)? "))
years = 0 

while initial_investment < target_value:                            # Will loop through working out the current amount until that surpasses the target value
    initial_investment = initial_investment * (1 + interest_rate/100)   # Because the user is putting the interest rate in as a percentage that needs to be converted into a decimal
    years = years + 1                                               # Each iteration is the equivalant of a year 
print(f"In {years} years your initial investment will grow to your target value (£{target_value})300")
print(f"After {years} years you will have £{round(initial_investment,2)}")

# Part 4 - Input an integer between two limits
min_num = 1     # Variable that declares what the minimum value is 
max_num = 100   # Variable that declares what the maximum value is 
attempts = 0 

while attempts < 3:         # While loop will run if the user enters a number that isout of range untill they enter 3 numbers thare out of range 
    user_num = int(input(f"Please enter a number between {min_num} and {max_num}. "))

    if min_num <= user_num <= max_num:  # If they enter a value that is in range then the while loop will automatically stop
        print(f"Valid number entered: {user_num}")
        break
    else:
        print("Invalid number entered. Please try again.")
    attempts = attempts + 1 

if attempts == 3:
    print("None")

# Part 5 - count vowels
word = input("Enter a word: ")

counter = 0     # Counter is used as a placeholder when iterating through the word
vowels = 0 

while counter < len(word):
    letter = word[counter]  # The letter that is currently being iterated is the value of counter
    if letter in "aeiou":
        vowels = vowels + 1 # Every time the letter = a vowel the vowel variable will be incremented
    counter = counter + 1
print(f"In {word} there are {vowels} vowels.")

# Part 6 - exam average

maths_mark = int(input("Enter your Maths mark (0-100): ")) # Asks the user for their maths grade and will check to see if it is a valid mark before performing any calculations
while 0 < maths_mark < 100:
    print(f"Valid Maths mark entered {maths_mark}.")
    break 

english_mark = int(input("Enter your English mark (0-100): "))  # Asks the user for their english grade and will check to see if it is a valid mark before performing any calculations
while 0 < english_mark < 100:
    print(f"Valid English mark entered {english_mark}.")
    break

ict_mark = int(input("Enter your ICT mark (0-100): "))          # Asks the user for their ict grade and will check to see if it is a valid mark before performing any calculations
while 0 < ict_mark < 100: 
    print (f"Valid ICT mark entered {ict_mark}.")
    break

average_mark = (maths_mark + english_mark + ict_mark) / 3       # Works out the users average mark across the three papers

if average_mark >= 65:      # Checks to see if they passed or failed based off of the IF statement
    result = "Pass"
else:
    result = "Fail"

print(f"Your average mark is: {round(average_mark, 2)}. This is a {result}")


# Task 2 

# Part 1 - squares using FOR loop

for i in range (1,101):                 # Same as a previous task but using a FOR loop instead of a WHILE loop
    square = i ** 2                     # Uses the range of values to iterate through until the square value is greater than 2000 or the end of the range is reached
    if square > 2000:
        break
    print(f"{i} squared = {square}")

# Part 2 - factorial using FOR loop     # Same as a previous task but using a FOR loop instead of a WHILE loop

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i
print(f"The factorial of {num} = {factorial}")

