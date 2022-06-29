#！python
# Saves and loads pieces of text to the clipboard.
# Usage:
# python multiclipboard.py save <keyword> - Saves keyword to clipboard.
# python multiclipboard.py <keyword> - Loads keyword to clipboard. 
# python multiclipboard.py list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('multiclipboard/mcb')

# Save clipboard content. 
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content. 
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
else:
    print(
        '''
    Command Unknown: cannot recognize your command.

    You can input in command lines as follows:
        - python multiclipboard.py save <keyword> - Saves keyword to clipboard.
        - python multiclipboard.py <keyword> - Loads keyword to clipboard.
        - python multiclipboard.py list - Loads all keywords to clipboard.
        '''
    )

mcbShelf.close()