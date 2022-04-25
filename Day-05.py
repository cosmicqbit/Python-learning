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
