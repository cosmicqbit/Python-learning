# Setup, Numbers, Strings & other Data Types

print("Hello World")
# name = input("What's your name? \n")
# print("Hello! " + name + " Welcome to the world of idiots ")

# Arithmetic Operations
print(3 / 2 ) # Division
print(3 + 8) # Addition
print(2 ** 3) # Exponent
print(5 // 2) # Floor Division
print(4 % 3) # Modulus Division
# for a%b => a = q * b + remainder

# Complement Assignments 
num = 5 
num = num + 2
num += 2

#Absolute value
print(abs(-2)) # will return 

#Round value 
print(round(2.4)) # will return 2 
print(round(2.334, 1)) # round off to 2 decimal place

#Comparisons 

3 == 2
2 != 23
3 > 2
2 <  1
4 >= 2
2 <= 4

# Identifier / Variable

name = "File"
print(name)

#Strings 

message = "test message"

#Multi line strings

line = """ This is a multi 
line string"""

print(line)

# Functions vs Methods

print(abs(-2.3)) #Function example

# Method

# Method is a specific function associated to a class called using dot

print(message.upper())
print(line.lower())

print(line.count('i'))
print(message.replace('test', 'gargantum'))

# Indexing 

box = 'Shariq Raza Qadri'
print(box[4:8]) # First index is inclusive & last index is not
print(box[:3]) #Slicing 
print(box[4])

# Concatenation

first_name = 'Shariq'
last_name = 'Raza Qadri'
greeting = 'Salaams'

greet = greeting + " " + first_name + " " + last_name
print(greet)

# Formatted String(s)

greet = 'Welcome {}. {}!'.format(greeting,name)
greet = f'Welcome  {greeting} {name}'

# Concatenating numbers / Type casting

num1 = 2
num2 = 3

num1 = int(num1)
num2 = int(num2)

print(num1 + num2)