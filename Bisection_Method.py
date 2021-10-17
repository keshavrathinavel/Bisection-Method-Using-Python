#Bisection method algorithm according to the working of the algorithm as taught in class

def f(x):

    # Here, we write the equation required to pass through the Bisection method
    return (x**3 - 5*x + 1)

def bisect(a, b, n):
    # We require an iterator to traverse the loop for a given number of iterations
    i = 1

    # Declaring a variable with a default true value for an infinite loop, the loop
    # terminates when the condition is not met - more details within the loop
    condition = True
    
    while condition:

        # Finding a midpoint within the given interval
        x = (a+b)/2

        # Condition for a negative root output
        if f(x<0):
            a = x

        # Condition for a positive root output
        else:
            b = x
        print("iteration = ", i, "x = ", x, "f(x) = ", f(x))

        # Terminating the loop when the iterator (i) reaches maximum iterations
        if i == n:
            condition = False
        
        # If the iterator is not at the maximum iterations, the loop continues 
        else:
            condition = True
            # Incrementing the iterator per iteration
            i = i+1

    # Outputting the value of the root after computation
    print("The required root is: ", x)

# Obtaining values for each required variable from the user
a = float(input("Enter the first approximation: "))
b = float(input("Enter the second approximation: "))
n = int(input("Number of iterations: "))

# Condition so that an erroneous/incorrect function is avoided
if f(a)*f(b) > 0:
    print("Given approximations are incorrect.")

# Execution of the algorithm
else: 
    bisect(a, b, n)
