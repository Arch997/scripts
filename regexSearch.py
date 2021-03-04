# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:19:00 2019

Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.

1. Import os and re
2. create a variable to open folder with ? call folder with listdir
3. create variable to store the folder variable in read() mode
4. TODO: Check if you can specifically read text files only
a. If yes, iterate over all files in folder name, read text files specifically
b. Else, check for the file extension of files with endswith() method. If .txt in files in folder, store the results of the iterated files in a variable
c. Create new directory with os.mkdir()
d. Iterate over the contents of new directory and assign the text folder variable contents to the new dirctory using os.path.join()
5. open the new directory in read() mode
6. Call re.compile on the .txt files with user-supplied regex. 
7. Search for match object
8. Print match objects if found, else, return None error message

@author: HP PC
"""

import os, re, glob, shutil

folder = os.getcwd()
folderList = os.listdir(folder)
#print(folderList)

# Using the filter function and lambda to extract text files from folder list. The filter function returns a filter object which returns a list of items when iterated over
txtfiles = filter(lambda x: x[-4:] == '.txt', folderList)
	

# Using glob to extract only text files from the folder. It returns a list value of all the text files	
txt_files = glob.glob('C:\\Users\\HP PC\\practice projects\\*.txt')



for files in glob.glob('C:\\Users\\HP PC\\practice projects\\*.txt'):
	fileList = open(files)	
	fileContent = fileList.read()
	print(fileContent)
	fileRegex = re.compile(r'Bacon')
	mo = fileRegex.findall(fileContent)
	print(mo)

	
'''for foldername, subfoldera, filenames in os.walk(folder):
	for filename in filenames:
		fullpath = os.path.join(folder, filename)
		with open (fullpath, 'r') as f:
			fc = f.read()
			fileRegex = re.compile(r'Quiz|quiz')
			mo = fileRegex.findall(fc)
			print(mo)'''

		
fileList.close()