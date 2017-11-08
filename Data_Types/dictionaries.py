# Create a dictionary called 'a'
a = {'Bob' : 77566, 'Fred' : 98311, 'Jackie' : 10523, 'Jane' : 54865}

print(a['Bob']) # Display the value in a dictionary by calling the key

a['Kyle'] = 65892 # Add key called 'Kyle' with a value of 65829

print(list(a.keys()))   # Display all of the keys
print(list(a.values())) # Display all of the values

# Create a dictionary called 'b' using the dict() constructor
b = dict([('Bob', 77566}, ('Fred', 98311), ('Kyle', 65892)])
print(b) # Display the new dictionary
