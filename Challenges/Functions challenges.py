# Password checker

def password_checker(password):
    unsafe_passwords = ["qwerty", "QWERTY", "123456", "password1", "123456789", "111111"]
    if password in unsafe_passwords:
        return(f"Use a safer password. {password} is easily guessable.")
    else:
        return("Your password is safe.")

# -------MAIN CODE-----------
password = input("Enter your password: ")
check_password = print(f"{password_checker(password)}")

# Simple calculator

def calculator(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    return(f"{num1} + {num2} = {addition} \n{num1} - {num2} = {subtraction} \n{num1} * {num2} = {multiplication}")

# -------MAIN CODE-----------
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
calculation = print(f"{calculator(num1, num2)}")

# Highest number returned 

def highest_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return (f"{num1} is the highest number.")
    elif num2 > num1 and num2 > num3:
        return (f"{num2} is the highest number.")
    elif num3 > num1 and num3 > num2:
        return (f"{num3} is the highest number.")
    elif num1 == num2 == num3: 
        return ("All numbers are the same, therefore there is not a highest number.")
    else:
        return ("Invalid input.")
    
#-------MAIN CODE------------
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

calculation = print(highest_num(num1, num2, num3))

# Checks if user input is odd or even
 
def odd_or_even(number):
    if number % 2 ==0:
        return(f"{number} is even. ")
    else:
        return(f"{number} is odd.")

#-------MAIN CODE-----------
number = int(input("Enter a number: "))
calculation = print(odd_or_even(number))

# Convert user input to capitals

def upper_case(word):
    return (word.upper())

#-------MAIN CODE-----------
word = input("Enter any word and it will all be made uppercase: ")
change_word = print(upper_case(word))

# Area of a circle

import math 

def circle_area(radius):
    area_of_circle = math.pi * radius ** 2
    return area_of_circle

#-------MAIN CODE-----------
radius = int(input("What is the radius of the circle? "))
calculation = print(f"{round(circle_area(radius),2)}")

# Temp converter 

def temp_converter(degrees_celcius):
    fahrenheit = (degrees_celcius * 1.8) + 32
    return (f"{degrees_celcius} (degrees c) in faharenheit is {fahrenheit}")

#-------MAIN CODE-----------
degrees_celcius = int(input("Enter the temperature in degrees celcius: "))
calculation = print(temp_converter(degrees_celcius))