# Reading Writing & Parsing Files

# Files --> Named collection of records stored into the secondary memory
# File characteristics --> Name + Extension

content = open('payload.txt', 'r')
content.close() # Have to Explicitly close it in order to not to run out of file descriptors

# "r" - Read : Default value. Opens file for reading
# "a" - Append : opens a file for appending, creates the file if it does not exist
# "w" - Write : Opens a file for writing, creates the file if it does not exist
# "x" - Create : Creates the specified file, returns an error if the it does not 

# Printing the file name
print(content.name)

# Check the file mode
print(content.mode) # In the case will return 'r' : reading mode

# Context Manager --> Handles file closing without explicity declaring that
with open('payload.txt', 'r') as content:
    print(content.read()) # Prints / Reads the file content
    pass

# Outside Context Manager 
# Check if file is closed
print(content.closed) # Will return bool

