#! python3
# Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add asterisk to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
