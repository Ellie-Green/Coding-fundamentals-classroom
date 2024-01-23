# Had to use Replit to run the code as python was playing up 

# Count task
def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum


# Factorial task
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


# List of squares task
def list_of_squares(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = i * i
    return d 