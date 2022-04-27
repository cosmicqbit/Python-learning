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