def myAdd(num1, num2):
    """The myAdd function takes two arguments (num1 and num2) and
    adds them together to create a nre variable (arg_sum) which
    is returned to the user. The value needs to be printed outside
    of the function either by passing it to a new variable or
    wrapping it in the print() method."""

    # Test the types 
    if isinstance(num1, str):
        try:
            num1 = float(num1)
        except ValueError:
            print('The first value needs to be a number.')
            return # returns None if the value cannot be converted.
    else:
        num1 = float(num1)
        
    if isinstance(num2, str):
        try:
            num2 = float(num2)
            return num1 + num2
        except ValueError:
            print('The second value needs to be a number.')
    else:
        num2 = float(num2)
        return num1 + num2


# TESTING:

# Call myFunc() and pass two numbers through it and then print
# the total value.
total1 = myAdd('3', 6)
print(total1)

total2 = myAdd('three', 6)
print(total2)

total3 = myAdd(3, '6')
print(total3)

total4 = myAdd(3, 'six')
print(total4)

total5 = myAdd(3, 6)
print(total5)
