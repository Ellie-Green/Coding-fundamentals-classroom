# Calculate the largest number not using an IF statement
#num1 = int(input("Enter a number: ")) 
#num2 = int(input("Enter a number: "))

#while num1 > num2:
#    print(f"{num1} is greater than {num2}")
#    break
#else:
#    print(f"{num2} is greater than {num1}")

# Calculates the largest number using no built in function
#num1 = int(input("Enter your first number: "))
#num2 = int(input("Enter your second number: "))

#largest = num1*(num1>num2) + num2*(num2>+num1)  # If num1>num2 then the first bracket will be 1 and the second will be 0. # Vice versa if num2 is the largest number

#print(f"{largest} is the bigger number.")


# Milkshake task 

#Sam has been dumped by his girlfriend so he's gone into the local milk
#bar to drown his sorrows. He has a budget, and there's a choice of three (or more)
#milkshakes,
#differently priced. The barman says, "What can I fix you?" and Sam can reply with a
#number corresponding
#to the relevant flavour - this list is displayed every iteration.
#If he enters Q, he quits and leaves; the barman wishes him well in his search for love.
#If he orders but can't pay he's thrown out.

#budget = int(input("What is your budget? "))
#milkshakes = {
#    1: {"flavour": "Chocolate", "price": 3},
#    2: {"flavour": "Vanilla", "price": 2.5},
#    3: {"flavour": "Strawberry", "price": 4},
#}

#while True:
#    print("\nMilkshake Menu:")
#    for number, shake in milkshakes.items():
#        print(f"{number}: {shake['flavour']} - £{shake['price']}")

#    choice = input("Enter the number of the milkshake you want (Q to quit): ").upper()

#    if choice == 'Q':
#        print("Goodbye! We wish you well in your search for love.")
#        break

#    try:
#        choice = int(choice)
#    except ValueError:
#        print("Invalid input. Please enter a number or 'Q' to quit.")
#        continue

#    if choice not in milkshakes:
#        print("Invalid choice. Please select a valid milkshake number.")
#        continue

#    selected_shake = milkshakes[choice]
#    if selected_shake["price"] > budget:
#        print("Sorry, you can't afford that milkshake. Get out!!")
#        break
#    else:
#        print(f"You've chosen {selected_shake['flavour']} milkshake. Enjoy!")
#        budget -= selected_shake["price"]

#    print(f"You spent £{10 - budget} at the milkshake bar.")

# Functions exercise
#def addition(num1, num2):
#    return (f"{num1} + {num2} = {num1 + num2}")

#print(addition(4,4))

