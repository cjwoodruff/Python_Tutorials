def myAdd(num1, num2):
    """The myAdd function takes two arguments (num1 and num2) and
    adds them together to create a nre variable (arg_sum) which
    is returned to the user. The value needs to be printed outside
    of the function either by passing it to a new variable or
    wrapping it in the print() method."""

    # Test the data types and convert to a float value if it isn't one
    # already. The best way to handle this is through the isinstance()
    # method.
    if isinstance(num1, str):
        try:
            num1 = float(num1)
        except ValueError:
            print('The first value needs to be a number.')
    else:
        num1 = float(num1)
        
    if isinstance(num2, str):
        try:
            num2 = float(num2)
        except ValueError:
            print('The second value needs to be a number.')
    else:
        num2 = float(num2)
        
        # This is nested inside the last else statement to return a
        # float value if and only if it is a float. Otherwise it will
        # return 'None'
        return num1 + num2


# TESTING:

# Call myFunc() and pass two numbers through it and then print
# the total value.
total = myAdd('3.5', 'six')
print(total)

# This shows that we don't necessarily need to assign the value
# to a variable. We can just print it out.
print(myAdd(3.5,6.5))
