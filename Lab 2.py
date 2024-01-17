# Part 1 - using only if
person = int(input("Enter your age: ")) # Asks the user for their age

if person >= 18:
    print("You are in category A")      # Performs an IF statement to determine what category they are in. 

if person >= 16:                        # This will cause a conflict in results for certain agaes as they will satisfy multiple if statements 
    print("You are in category B")

if person < 16:
    print("You are in category C")

# Part 1 - using elif
person = int(input("Enter you age: "))  # Using an IF/ ELIF statement will prevent multiple statements from being outputted. 

if person >= 18:                        # This is because the next IF statement will only run if the previous one is not met
    print("You are in category A")
elif person >=16:
    print("You are in category B")
else:
    print("You are in category C")

# Part 2 - create a calculator
num1 = float(input("Enter your first number: "))   # Takes in two inputs from the user
num2 = float(input("Enter your second number: "))
answer = ()

print("Calculator menu: ")      # Prints out the calculator menu
print("Add +")
print("Subtract -")
print("Multiply *")
print("Divide /")
print("Square **")

operation = input("From the above list select the operation you would like to perform: ")
if operation == "Add" or operation == "+":  # Depending on the operation that the user picked, the code will run the appropriate if statement which will work out the answer and output it
    answer = num1 + num2
    print(f"Answer = {answer}")
elif operation == "Subtract" or operation == "-" :
    answer = num1 - num2
    print(f"Answer = {answer}")
elif operation == "Multiply" or operation == "*" :
    answer = num1 * num2
    print(f"Answer = {answer}")
elif operation == "Divide" or operation == "/" :
   answer = num1 / num2
   print(f"Answer = {answer}")
elif operation == "Square" or operation == "**" :
    answer = num1 ** num2
    print(f"Answer = {answer}")
else:
    print("Operation not found.") 

# Part 2 - calculate exam grades
exam_mark = int(input("Enter your exam mark: ")) # Asks the user to input their mark

if exam_mark >= 71 and exam_mark <= 100:         # Will check to see what range the mark is in and it will run the corresponding if statement
    print("You got a distinction!!!")
elif exam_mark >= 61 and exam_mark <=70:
    print("You got a merit!!")
elif exam_mark >= 51 and exam_mark <=60:
    print("You got a pass!")
elif exam_mark < 50 and exam_mark >=1:
    print("You failed")
else:
    print("Incorrect mark entered.")

#Part 3 - calculate exam grades with levels
exam_mark = int(input("Enter your exam mark: "))        # Very similar to the previous task other then it runs the range check depending on what level the user inputs 
exam_level = int(input("Enter your exam level: "))

if exam_level == 1: 
    if exam_mark >= 71 and exam_mark <= 100:
        print("You got a distinction!!!")
    elif exam_mark >= 61 and exam_mark <=70:
        print("You got a merit!!")
    elif exam_mark >= 51 and exam_mark <=60:
        print("You got a pass!")
    elif exam_mark < 50 and exam_mark >=1:
        print("You failed")
    else:
        print("Incorrect mark entered.")

elif exam_level == 2:
    if exam_mark >= 66 and exam_mark <= 100:
        print("You got a distinction!!!")
    elif exam_mark >= 51 and exam_mark <=65:
        print("You got a merit!!")
    elif exam_mark >= 40 and exam_mark <=50:
        print("You got a pass!")
    elif exam_mark < 40 and exam_mark >=1:
        print("You failed")
    else:
        print("Incorrect mark entered.")
else:
    print("Incorrect level entered.")


# Part 4 
import math     # Imports the built in maths function so that square-root can be performed later in the code

print("Pythagoras calculator: ")
print("1. Find length of A given B and C")  # Prints out the menu to the user so they can pick th option they want based off of what sides they arlready know the length for
print("2. Find length of B given A and C")
print("3. Find length of C given A and B")

answer = ()         # Pythagorus = square root (A**2 + B**2)
operation = int(input("Enter the calculation you want to perform: "))

if operation == 1:      # The option selected by the user will determine which calculation is performed 
    side_B = int(input("Enter the length of side B: "))
    side_C = int(input("Enter the length of side C: "))
    answer = math.sqrt(side_B ** 2 + side_C ** 2)
    print(f"Length of A = {answer}")
elif operation == 2:
    side_A = int(input("Enter the length of side A: "))
    side_C = int(input("Enter the length of side C: "))
    answer = math.sqrt(side_A ** 2 + side_C ** 2)
    print(f"Length of B = {answer}")
elif operation == 3:
    side_A = int(input("Enter the length of side A: "))
    side_B = int(input("Enter the length of side B: "))
    answer = math.sqrt(side_A ** 2 + side_B ** 2)
    print(f"Length of C = {answer}")
else:
    print("Incorrect input.") 


