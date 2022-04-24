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

# Checking leap year
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



