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

