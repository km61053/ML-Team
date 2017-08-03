import re

def matchText(text):
    pattern = '^[a-zA-Z0-9_]*$'
    if re.search(pattern, text):
        return 'Match Found'
    else:
        return 'Not Match found'

print (matchText("This is a smaple python program using functions"))
print (matchText("Python_Sample_Program_123"))


