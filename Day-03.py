# Condtions & Loops

# If
num = 10
if num % 2 == 0:
    print('Num is an even number')

# If else
if True: 
    print('This is the new line')
else:
    print("This line won't execute")

num = 15 
if num % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

# else if
city = 'Chennai'
if city == 'Bangalore':
    print('City is Bangalore')
elif city == 'Chennai':
    print('City is Chennai')
else:
    print('Not matching')

grade = 10
if grade == 10:
    print("Your score is A")
elif grade == 9:
    print("Your score is B")
elif grade == 8:
    print("Your score is C")
else:
    print("You've failed")

# Conditional Operators

user = 'Admin'
logged_in = False

if user == 'admin' and logged_in:
    print('Admin Page')
else:
    print('Wrong credentials')

# Not operators

user = 'Admin'
logged_in = True

if not logged_in:
    print('Please log in')
else:
    print('Welcome!')


# check equality of lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1)
print(list2)

print(list1 == list2) # Will return boolean

 # Comparing List IDs
print(list1 is list2) # Will return false 

print(id(list1))
print(id(list2))



