#! python3
# mcb.pyw - Multiclipboard
# A program that can save and load pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Load keyword to clipboard.
#        py.exe mcb.pyw list - Load all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        # Save clipboard to keyword.
        mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        # Copy list of keywords to clipboard.
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        # Load the keyword to the clipboard.
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
