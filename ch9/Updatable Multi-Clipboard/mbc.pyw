#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mbcshelve = shelve.open('mbc')

#  Save clipboard content.
if len(sys.argv) > 3:
    if sys.argv[1].lower() == 'save':
        mbcshelve[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mbcshelve:
        del mbcshelve[sys.argv[2]]

elif len(sys.argv) == 2:
    #  List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mbcshelve.keys())))
    elif sys.argv[1].lower() == 'delete':
        mbcshelve.clear()
    elif sys.argv[1] in mbcshelve:
        pyperclip.copy(mbcshelve[sys.argv[1]])



mbcshelve.close()