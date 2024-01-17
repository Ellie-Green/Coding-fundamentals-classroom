def get_income_tax(salary):
    personal_allowance = 11850
    basic_rate_threshold = 34000
    higher_rate_threshold = 150000

    if salary <= personal_allowance:
        return 0    # No tax if salary is within personal allowance
    elif personal_allowance < salary <= basic_rate_threshold:
        return 0.2 * (salary - personal_allowance)  # 20% tax for income in basic rate
    elif basic_rate_threshold < salary <= higher_rate_threshold:
        return (0.2 * (basic_rate_threshold - personal_allowance)) + (0.4 * (salary - basic_rate_threshold))    # 20% tax for income in basic rate, 40% tax for income in higher rate
    else:
        return (0.2 * (basic_rate_threshold - personal_allowance)) + (0.4 * (higher_rate_threshold - basic_rate_threshold)) + (0.45 * (salary - higher_rate_threshold)) # 20% tax for income in basic rate, 40% tax for income in higher rate, 45% tax for income over 150,000


#------------------------Main Code---------------------------
salary = int(input("Please enter your salary: "))
tax = get_income_tax(salary)

print(f"Income tax for salary £{salary} is £{tax}")