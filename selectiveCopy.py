# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:26:58 2019

Selective Copy
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

#! python3
# selectiveCopy.py 
1.  import os, shutil
2. Get working directory
3. Walk through the directory tree using os.walk()
b. iterate over files in the tree
c. Iterate specifically over files that have a .pdf extension
d. For each file found, print the file to the console
e. Copy the found files to another location with shutil.copy()

@author: HP PC
"""

import os, shutil, glob
from contextlib import ExitStack

def selectCopy():
	dstDir = input('Copy destination: ') # Destination folder or file where source will be copied to
	dstDir = os.path.abspath(dstDir)
	srcDir = input('Copy source: ')
	srcDir = os.path.abspath(srcDir) # Source folder to walk through
	ext = input('File extension of files you want to copy: ')
	os.chdir(srcDir)
	for foldername, subfolders, filenames in os.walk(srcDir):
			for filename in filenames:		
				#filename = os.path.abspath(filename)
				if filename.endswith('%s' %(ext)):
					filename = os.path.abspath(filename)
					fullPath = os.path.join(srcDir, filename)
					print(filename)
					shutil.copy(fullPath, dstDir)
	print('Done')
					
selectCopy()
