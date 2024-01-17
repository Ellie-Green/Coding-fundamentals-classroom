import statistics                   # Imports the built in funtion of statistics to help with later calculations

# Part 1 
data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = (data.split(","))          # Extracts the values from the string and stores them in a list by spliting the original string at the ","
grades = list(map(int, grades))     # Casts all the elements from a list of string to a list of integers

min_grade = min(grades)             # Uses the built-in funtion of min to get the minimum grade in the list 
max_grade = max(grades)             # Uses the built-in function of max to get the maximum grade in the list

print(f"From the list, the lowest grade is {min_grade}.")
print(f"From the list, the highest grade is {max_grade}.")

average = sum(grades) / len(grades) # Works out the average by using the built in function for getting the sum of the list and dividing it by the length of the list. 
print(f"The average for the grades = {round(average,2)}")

mean = statistics.mean(grades)      # Uses the statistics function to work out the mean without having to manually code the calculation steps
print(f"The mean for the grades = {round(mean,2)}")

median = statistics.median(grades)  # Uses the statistics function to work out the median without having to manually code the calculation steps
print(f"The median for the grades = {median}")

x = "The minimum value is {}. The maximum value is {}. Average = {}. Mean = {}. Median = {}"
print (x.format(min_grade, max_grade, round(average,2), round(mean,2), median)) # Uses formating to print out the end statement based of the positon of arguements