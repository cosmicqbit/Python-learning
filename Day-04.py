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

