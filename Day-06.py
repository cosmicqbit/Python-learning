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

# Reading files line by line

with open('payload.txt', 'r') as content:
    file_content = content.readlines()
    print(file_content) # Will return all the lines in one single string

with open('payload.txt', 'r') as content:
    file_content = content.readline() # will return first line only
    print(file_content)
    file_content = content.readline()
    print(file_content) # Reads 2nd line to the screen cuz pointer have moved to the next line 

    # adds new empty line character between two consecutive lines
    # Fix above problem 

    file_content = content.readline()
    print(file_content, end='')

    file_content = content.readline()
    print(file_content, end='')

# Looping through all the lines using loop

with open('payload.txt') as content:
    for line in content:
        print(line, end='')

