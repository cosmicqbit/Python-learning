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

# Reading specific no of chars

with open('payload.txt') as content:

    file_content = content.read(10)
    print(file_content, end='*')

    file_content = content.read(20)
    print(file_content, end="-")

# Better way : To avoid returning empty chars even after the content lines have exhausted

with open('payload.txt', 'r') as sample:
    size_to_read = 10
    sample_content = sample.read(size_to_read)
    while len(sample_content) > 0:
        print(sample_content, end='*')
        sample_content = sample.read(size_to_read)

# Get position of the pointer while file reading

with open('payload.txt', 'r') as source:
    size_to_read = 20
    f_contents = source.read(size_to_read)
    print(source.tell()) # Will return 20 

# Changing the position of pointer to desired index

with open('payload.txt', 'r') as dump:
    size_to_read = 10
    turnout = dump.read(size_to_read)
    print(turnout, end='')

    f.seek(0)

    turnout = dump.read(size_to_read)
    print(turnout, end='') # Will return the first 10 chars again

# --------------- #

# Writing in the file

with open('payload.txt', 'w') as notebook:
    notebook.write('Bismillah') ## WARN : Will overwrite all the existin text as it starts form index 0

with open('dummy.txt', 'w') as so:
    pass # Will create the file if it doesn't exist

with open('dummy.txt', 'w') as horse:
    horse.write('Grass') # Will write the 'Grass' string to the the dummy.txt 

# Copying to a new file

with open('payload.txt', 'r') as rf:
    with open('dummy.txt', 'w') as wf:
        for line in rf:
            dummy.write(line)

# Copying image using binary method 'rb' & 'wb' 

with open('source.png', 'rb') as image:
    with open('destination.png', 'wb') as copied_pic:
        for line in image:
            copied_pic.write(line)


