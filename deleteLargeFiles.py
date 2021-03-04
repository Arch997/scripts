# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:04:50 2019

Deleting Unneeded Files
It’s not uncommon for a few unneeded but humongous files or folders to
take up the bulk of the space on your hard drive. If you’re trying to free up
room on your computer, you’ll get the most bang for your buck by deleting
the most massive of the unwanted files. But first you have to find them.
Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB. (Remember, to get a file’s size, you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.

# Write a function that will delete files larger than a specified size from a specified folder 

1. import os, shutil
2. Change directory to location you want to point to
3. Write a function to perform the task. It will take in a folder as argument
a. Walk through the folder tree
b. Search through folders
c. Iterate through files in folders: Assign absolute path to file. Create a fileInfo obj for files in folders through os.path.getsize(). Print the size of the file(s) found
d. Write conditional statement: If file is up to or larger than 100MB, print file
e. If all checks out, delete file with os.unlink()

@author: HP PC
"""
import os, shutil

def deleteLarge(folder):
	for foldernames, subfolders, filenames in os.walk(folder):
		#print('Deleting large, unwanted files in %s...' %(foldernames))
		for subfolder in subfolders:
			for filename in filenames:
				# Assigning absopute path to filename recursiely
				filename = os.path.abspath(filename)
				#print('Size of %s is: ' %(filename), end='')
				#print(os.path.getsize(filename))
				if os.path.getsize(filename) > 1000000000:
					os.unlink(filename)
					

deleteLarge('C:\\Users\\HP PC\\practice projects')			