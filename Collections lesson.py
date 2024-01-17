# My solution 
# Dictionary of books for 3 Authors 
books_dict = {"Roald Dahl": ["Charlie and the chocolate factory", "Fantastic Mr Fox", "James and the Giant peach", "Matilda"], "Michael Morpurgo": ["War Horse", "Private Peaceful", "Shadow", "Running wild"], "Colleen Hoover": ["It ends with us", "Ugly love", "Hopeless", "Confess"]}
author = input("Please pick either, Roald Dahl, Michael Morpugo or Colleen Hoover: ") # Asks for a user input

if author == "Roald Dahl": # Depending on what the user input is it will output the corresponding list of books
    print ("Roal Dahl has written: " + ",".join(books_dict["Roald Dahl"])) # Join function turns the dictionary into a string to make the output easier to read for the user
elif author == "Michael Morpurgo":
    print ("Michael Morpurgo has written: " + ",".join(books_dict["Michael Morpurgo"]))
elif author == "Colleen Hoover":
    print ("Colleen Hoover has written: " + ",".join(books_dict["Colleen Hoover"]))
else: # If the user enters a name that is no in the dictionary then a message will be outputted to the user. 
    print ("Author not found.")

# Different solutions
books_dict = {"Roald Dahl": ["Charlie and the chocolate factory", "Fantastic Mr Fox", "James and the Giant peach", "Matilda"], "Michael Morpurgo": ["War Horse", "Private Peaceful", "Shadow", "Running wild"], "Colleen Hoover": ["It ends with us", "Ugly love", "Hopeless", "Confess"]}
y = input("Enter author name: ")
books = books_dict.get(y, []) # The get method will search the dictionary based off of what the user entered
print(",".join(books) or "Author not found.") # Outputs the list of books that the get method collected. # Join function turns the list into a string 
