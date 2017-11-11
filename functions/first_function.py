def myAdd(num1, num2):
    """The myAdd function takes two arguments (num1 and num2) and
    adds them together to create a nre variable (arg_sum) which
    is returned to the user. The value needs to be printed outside
    of the function either by passing it to a new variable or
    wrapping it in the print() method."""
    
    arg_sum = num1 + num2
    return arg_sum


#TESTING:

# Call myFunc() and pass two numbers through it and then print
# the total value.
total = myAdd(3, 6)
print(total)

# This shows that we don't necessarily need to assign the value
# to a variable. We can just print it out.
print(myAdd(3, 6))
