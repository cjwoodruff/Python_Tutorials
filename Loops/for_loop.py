# Detail a tuple of lists of strings
tup = (['First', 'Name', 'Here'],
       ['Last', 'Name', 'Here'],
       ['Phone', 'Number', 'Here'],
       ['Full', 'Address', 'Here'])

# Iterate through each list in the tuple
for i in tup:
    print(i) # Display the list
    
    # Iterate through each word in the list
    for word in i:
        print(word) # Display the word in the list
        
        # Iterate through each letter in a word
        for letter in word:
            print(letter) # Display each letter in the word
