# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carla Gentry', 'Corinna Cortes']

# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)

# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)


# Create the Dictionary
courses = {'Math':65, 'English':70, 'History':80, 'French':70, 'Science':60}


# Slice the dict and stores  the all subjects marks in variable
total = list(courses.values())
total = sum(total)

# Store the all the subject in one variable `Total`
Total = courses.keys()
#print(len(Total))

# Print the total
print(total)

# Insert percentage formula
percentage = (total/(len(Total)*100))*100

# Print the percentage
print(percentage)



# Create the Dictionary
mathematics = {'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Bengio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}

vals = list(mathematics.values())
keys = list(mathematics.keys())
topper = max(vals)
print(keys[vals.index(topper)])

# Given string
topper = keys[vals.index(topper)] 

# Create variable first_name 
first_name = topper.split()[0]

# Create variable Last_name and store last two element in the list
last_name = topper.split()[1]

# Concatenate the string
full_name = last_name + " " + first_name

# print the full_name
print(full_name)

# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)

# Code ends here


