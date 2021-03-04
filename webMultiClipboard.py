# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:49:22 2019

• Open all links on a page in separate browser tabs.

1. copy a text page containing muliple web links to the clipboard

2. Paste the contents of the clipboard to a variable as a list of strings. If any string in that list starts with either 'http' or 'www' and ends with '.com', assign it to the variable

3. Iterate through the new list of links and call webbrowser.open() for each iteration of the loop to open each link in the link

@author: HP PC
"""

import pyperclip, webbrowser, traceback

linkText = []
text = pyperclip.paste()

try:
	linkText.append([links for links in text if(any(links.startswith('http') for i in text) or any(links.startswith('www') for i in text) and any(links.endswith('.com') for i in text))])

except:
	errorFile = open('errorInfo.txt', 'a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('the traceback info was written to errorInfo.txt')

'''for i in linkText :
	webbrowser.open(i)
assert any(text.startswith('http')) or any(text.startswith('www')), 'There are no links in text'''