# Functions

def func():
    pass # Not doing anything

func()

print(func) # Will return reference for the function

# /// ----- ///

def hello_func():
    return 'Hello people over the Internet'

hello_func() # Won't display any result 
print(hello_func()) # This will print the string in the output

string = hello_func() 
print(string) # Same as above

# // Modify above function //

def hello_func(name):
    return 'Hello, {}'.format(name)

print(hello_func('Shariq'))

# With a default value 

def greet(greeting, name='You'):
    return '{} {}'.format(greeting, name)

print(greet('hello', name='shariq'))
print(greet('Hey'))

# Here greeting is the required parameter
# And name is a named parameter / optional
# Required parameters should be supplied to the function first --> Also called Positional arguments
# Keyword argument | example: name='shariq'

#-----------------------#
# Dealing with unknown number of input arguments

def func(*args, **kwargs):
    print(args)
    print(kwargs)

# *args for the arbitrary no of positional arguments | will return tuple 
# *kwargs for arbitrary no of keyword arguments | will return dictionary

# Example 
func('COA', 'OS', name="Shariq", age='20')

# Supplying *args as List & **kwargs as Dictionary

def func(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['COA', 'OS']
info = {'name': 'Shariq', 'age':20}
func(courses, info) # Will return a single tuple, courses as list & info as dictionary
# Both courses & info gets supplied as positional args cuz no keyword is included

# Supplying courses & info as parg & kwarg respectively
courses = ['COA', 'OS']
info = {'name': 'Shariq', 'age':20}
func(*courses, **info)

# Checking leap year #
# -------------- #

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    # Return True for leap years, and False for non-leap years.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    # Return no of days in that month in that year.
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2024))
print(days_in_month(2024, 2))

# Function scope

def func(x):
    x += 2
    print('Function returned value =',x)

y = 10
print('Before function call y =',y)
func(y)
print('After function call y =',y)