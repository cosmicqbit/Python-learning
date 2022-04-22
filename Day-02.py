# Lists - A collection of elements
# Types: List, Tuple, Sets, Dictionary

# Array 
courses = ['coa', 'os', 'dsa', 'dbms']
print(courses)
print(len(courses)) # Returns the length
print(courses[0:3])

# Append -> Method to add element at the end
courses.append('probability')
print(courses)

# Insert -> Inserts elemetn at a specific index
courses.insert(0,  'architecture')
print(courses)

# Inserting list inside the list
courses2 = ['dsp', 'iwt']
courses.append(courses2)
print(courses)

# Extending the list / Merging list(s)
courses2 = ['dsp', 'iwt']
courses.extend(courses2)
print(courses)

# Removing / Deleting element from List
courses.remove('os')
print(courses)

# Removing last element particularly
terminal_element = courses.pop() # Returns the removed element
print(courses)

# Finding index of an element
print(courses.index('dsa'))
# Returns error if element doesn't exist 

# check if an element exists in the list
print('coa' in courses) # Returns boolean value





