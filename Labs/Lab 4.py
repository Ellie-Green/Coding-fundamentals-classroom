# Part 1 
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

# Length of ages 
length_of_ages = len(ages)
print(length_of_ages)

# Print each age on its own line
for age in ages: # Uses a FOR loop to get each age in the ages list and will print each one out on it own line
    print(age)

# Add one to each age
for i in range(len(ages)): # Checkes what the length of the list is to make sure all of the ages are ammended
    ages[i] += 1           # The age that is currently being iterated will get one added to it

print(ages)                # Once the FOR loop has finished the updated list will be printed 

# Remove ages
for age in ages:           # Loops through the ages list
    if age < 16 or age > 65:    # If the age is less than 16 or greater than 65 it will get removed from the list 
        ages.remove(age)

print(ages)                # The updated list is then outputted to user once the loop ends

# Count how many between 16 and 25
count = 0

for age in ages:           # Loops through the ages list
    if age >= 16 and age<= 25:  # Checks to see if the age is between 16 and 25
        count = count + 1       # If it is then the count variable will increase by one

print(count)               # Once the list has been iterated through, count will be printed to the user. Count = how many of the ages are between 16 and 25

# Sort ages
ages.sort()     # Sorts the ages in asending order
for age in ages:
    print(age)  # Prints out all the ages in the correct order 

# Proportion
count = 0 

for age in ages:
    if age >= 16 and age <= 25:     # Checks to see which ages are greater than 16 and less than 25 
        count = count + 1           # For every age between 16 and 25 count is increased by 1
proportion = count / len(ages)      # Works out the proportion of ages that are between 16 - 25 out of the whole list
print(proportion)

# Vowels
word = input("Enter a word: ")      # User enters a word and the amount of vowels in that word will be calculated
vowels = "aeiou"                    # States what the vowels are in a string
count = 0 

for letter in word:                 # Loops through every letter of the word that is inputted
    if letter.lower() in vowels:    # Checks to see if that letter is in the vowels string
        count = count + 1           # If it then count is increased and the loop continues. If its not then the loop will just continue

print(count)
