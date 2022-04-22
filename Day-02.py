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

# Sorting / Reversing elements in list
courses.reverse()
print(courses)

# Sorting --> Actually sorts the list
num = [2, 3, 5, 6, 0, 6]
num.sort()
print(num)
print(sorted(num)) # Returns sorted list but doesn't actually change the original list

# Sorting in reverse
num = [2, 3, 5, 6, 0, 9]
num.sort(reverse = True)
print(num)

# Finding min in the List
print(min(num))

# Finding max in the list
print(max(num))

# Sum 
print(sum(num))

# Merging the values in a common string
test = ['Amir', 'Saqib', 'Wajid', 'Shahid']
test_string = '-'.join(test)
print(test_string)