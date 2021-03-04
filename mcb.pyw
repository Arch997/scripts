# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:18:55 2019

You can write a Python program to keep track of multiple pieces of text.
This “multiclipboard” will be named mcb.pyw (since “mcb” is shorter to type
than “multiclipboard”). The .pyw extension means that Python won’t show
a Terminal window when it runs this program. (See Appendix B for more
details.)
The program will save each piece of clipboard text under a keyword.
For example, when you run py mcb.pyw save spam, the current contents of the
clipboard will be saved with the keyword spam. This text can later be loaded
to the clipboard again by running py mcb.pyw spam. And if the user forgets
what keywords they have, they can run py mcb.pyw list to copy a list of all
keywords to the clipboard.
Here’s what the program does:
• The command line argument for the keyword is checked.
• If the argument is save, then the clipboard contents are saved to the
keyword.
• If the argument is list, then all the keywords are copied to the clipboard.
• Otherwise, the text for the keyword is copied to the keyboard.
This means the code will need to do the following:
• Read the command line arguments from sys.argv.
• Read and write to the clipboard.
• Save and load to a shelf file.
If you use Windows, you can easily run this script from the Run… window
by creating a batch file named mcb.bat with the following content:
@pyw.exe C:\Python34\mcb.pyw %*
#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
u # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

@author: HP PC
"""
import pyperclip, shelve, sys, os

mcbShelf = shelve.open('mcb')

def removeFiles():
	mcbShelf.close()
	if sys.argv == 2 and sys.argv[1] == 'delete':
		os.remove('mcb.dir')
		os.remove('mcb.bak')
	return

if not sys.argv:
	print('No option entered')
	sys.exit()

spam = [] # For current contents of the clipboard
lists = [] # For all the contents of the clipboard copied
if len(sys.argv) == 3 and sys.argv[1] == 'save'.lower():
	mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
	#TODO list keywords and load contents
	if sys.argv[1].lower() == 'list':
		 pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		 pyperclip.copy(mcbShelf[sys.argv[1]])


#TODO Extending the Multiclipboard. Extend the multiclipboard program in this chapter so that it has a delete<keyword> command line argument that will delete a keyword from the shelf.Then add a delete command line argument that will delete all keywords.
if len(sys.argv) == 3 and sys.argv[1] == 'delete'.lower():
	if sys.argv[2] in mcbShelf:
		del mcbShelf[sys.argv[2]]
	print(sys.argv[2] + ' deleted')

elif len(sys.argv) == 2:
	 if sys.argv[1].lower == 'delete':
		 mcbShelf.close()
		 # Calling 'n' flag creates a new, empty database
		 mcbShelf = shelve.open('mcb', flag='n')
		 removeFiles()

#mcbShelf.close()