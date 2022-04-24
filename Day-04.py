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



