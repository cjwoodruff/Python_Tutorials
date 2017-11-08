x = [1, 2, 3] # Create the first list
y = [4, 5, 6] # Create the second list
t = (x, y)    # Create the tuple from the lists

print(t)       # Print the tuple
print(type(t)) # Display the type 'tuple'

print(t[0])    # Display the first list
print(t[0][1]) # Display the second element of the first list

a, b = t # Assign the first list to 'a' and the second list to 'b'
print(a) # Display the first list
print(b) # Display the second list

a[0] = 'sorry' # Assign 'sorry' to the first item in list 'a'
print(a)       # Display the list 'a'
print(x)       # Display how list 'x' has changed

c = 'Hello!',  # Display how a simple comma can accidentally create a tuple
print(type(c)) # Show that 'c' is now a tuple
