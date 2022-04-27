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
