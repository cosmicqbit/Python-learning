# List Slicing & Sorting

# Sorting
# Arranging elements in ascending or descending order

# Slicing --> Extracting certain elements from list or string

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 

print(my_list[0]) # Will return 0
print(my_list[-1]) # will return last element 

# Negative indexes come handy when we don't know the length of List

print(my_list[0:6]) # Will return numbers from 0 - 5 cuz the terminal index is not inclusive

print(my_list[:9]) # Will print from 0 to 8

print(my_list[4:10]) # Will print from 4 to 9
print(my_list[:10]) # Same as above

print(my_list[:]) # will print entire list

print(my_list[-7:-3]) # Will print 3 - 6

# End limit should be > start index in case of negative indexing
print(my_list[-3:-8]) # Wrong

# Slicing with steps
# Syntax -> list[start:end:step]
print(my_list[::1]) # will return all elements
print(my_list[::2]) # Will print even elements only 
print(my_list[1:10:2]) # will print 1, 3, 5, 7, 9

# Extractin list in reverse format
print(my_list[::-1]) # Will reverse the list

print(my_list[-2:2:-2]) # Start index must be lesser than ending index

# ---------------- #
# Slicing Strings

sample_url = 'https://cosmicqbit.dev'

print(sample_url)
print(sample_url[1])

# Reverse the URL
print(sample_url[::-1]) 

# Get the TLD
print(sample_url[-4:])

# Get the url without https:// 
print(sample_url[8:])

# Get cosmicqbit purely
print(sample_url[8:-4])

# ----------- #
# Sorting #

lis = [4, 5, 8, 9, 1, 0, 6, 7, 2, 3]

sorted_list = sorted(lis)

print('Sorted list is:\t', sorted_list)
print('Original List is :\t', lis)

# Sort Method
lis.sort()
print(lis) # Actually changes the original list

r = lis.sort() # Deosn't return any value for being a method & not a function

# Sorting in reverse

sorted_list = sorted(lis, reverse=True)
print(sorted_list)

# Sorting based on Absolute value in case of negative elements
li = [-5, -6, -8, -4, 1]
s_li = sorted(li, key=abs) # abs stand for absolute value
print(s_li)

# Sorting a tuple

tup = (2, 4, 6, 7, 9, 3)
sorted_tup = sorted(tup)
print(sorted_tup)

# Sort method can't be implemented on tuples

# Sorting a Dictionary

dict = {'name': 'Amir', 'job': 'teacher', 'age': 25, 'course': 'python'}
sorted_dict = sorted(dict)
print(sorted_dict) # Will print only keys in aplhabetical order 