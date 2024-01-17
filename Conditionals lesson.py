# Exercise 1
mark = int(input("Please enter your exam mark: ")) # Takes an input from the user
if mark > 85:                      # If statement will use conditional operators to see if the user got a pass, destinction or a fail in their test
    print("Distinction")
elif mark >= 65 and mark <=85:
    print("Pass")
else:
    print("Fail")

# Exercise 2
weight = float(input("Enter a weight: "))     
weight_metric = input("What metric is this weight in (Kgs or Lbs)? ")
print(f'You entered {weight} {weight_metric}.')

if weight_metric == "Kgs":
    lbs = weight * 2.205
    print(f'This weight converted to Lbs is: {lbs}.')
elif weight_metric == "Lbs":
    kgs = weight / 2.205
    print(f'This weight converted to Kgs is: {kgs}.')
else:
    print("Incorrect metric entered.")


