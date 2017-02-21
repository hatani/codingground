# Hello World program in Python

import re
    
greeting = 'Hello World!'
EOL = '\n'

regex = re.compile(r'Hella')
mo = regex.search(greeting)
if mo:
    print '"Mo" is there!'
else:
    print '"Mo" is not at home today.'