# Create a set called 'cars' and print the set out. Notice how the set drops
# all of the duplicate values.
cars = {'Ford', 'Chrysler', 'Chevrolet', 'Ford', 'Dodge', 'Dodge', 'Chevrolet', 'Ford', 'Mazda'}
print(cars)

# See if 'Dodge' is in 'cars' set
print('Dodge' in cars)

# See if 'Lincoln' is in 'cars' set
print('Lincoln' in cars)

# Create a set called 'fcars'
fcars = {'Mitsubishi', 'Honda', 'Mazda', 'Toyota'}

print(cars)         # Display the 'cars' set
print(fcars)        # Display the 'fcars' set
print(cars - fcars) # Display the set of cars that don't have the same values as fcars
print(cars | fcars) # Display both sets without duplicates
print(cars & fcars) # Display the item(s) that are in both sets
print(cars ^ fcars) # Display items from both lists that aren't in both lists
