# Regular Expression 
# Used to extract special sort of information following a certain pattern

import re

text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] ( )
cosmicqbit.dev
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Bean
Mr Mouse
"""

# Raw String
print('\Text String') # Will print five spaces before the text

# Print \t in the text
print(r'\tText String') # Will print \t as well 

# Finding a match of 'abc' string
pattern = re.compile(r'abc') 
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

print(text_to_search[1:4])

# . stands for every character cuz it's a MetaCharacter
pattern = re.compile(r'\.') # Adding \
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# Locating the URL
pattern = re.compile(r'cosmicqbit\.dev')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# .     - Any character Except new line
# \d    - Digit (0-9)
# \D    - Not a Digit (0-9)
# \w    - Word Character (a-z, A - Z, 0-9, _)
# \W    - Not a Word Character
# \s    - Whitespace (space, tab, newline)
# \S    - Not Whitespacce (space, tab, newline)

# Practice
pattern = re.compile('\w') # Try with . \d \D \w \W \s \S
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# Anchors

# \b    - Word Boundary
# \B    - Not a Word Boundary
# ^     - Beginning of a String
# $     - End of a String