# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:31:11 2019

#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

@author: HP PC
"""

import sys, pyperclip, webbrowser

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()
	
webbrowser.open('https://www.google.com/maps/place/' + address)

