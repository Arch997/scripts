# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:19:38 2019

@author: HP PC
"""

# Find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space

import os, glob

numFiles = 0
numFolders = 0
folderSize = 0
totalSize = 0
largest = 0
mostFiles = 0
files = 0
fullSizes = 0

folder = 'C:\\Users\\HP PC'
os.chdir(folder)
largestFolder = []

folder = os.path.abspath(folder)

for foldernames, subfolders, filenames in os.walk(folder):
	#foldernames = os.path.abspath(foldernames)
	folderSize = os.path.getsize(foldernames)
	#print(f'{foldernames, folderSize}')
	if folderSize > int(largest):
		largest = folderSize
		if os.path.getsize(foldernames) == largest:
			largestFolder = foldernames + ": " + str(largest)
	numFolders +=1	
	fullSizes += os.path.getsize(foldernames)
	totalSize += fullSizes
			
	#print(foldernames)
	for subfolder in subfolders:
		folderSize = os.path.getsize(os.path.abspath
							   (subfolder))
		print(f'{subfolder, folderSize}')
		#print('SUBFOLDER is ...' + subfolder + '... in: ' + foldernames)
		for filename in filenames:
			numFiles += 1
			#print(f'{foldernames, filename, numFiles}')
			'''for filenames in foldernames:
				#numFiles += 1
				if numFiles > int(mostFiles):
					mostFiles = numFiles'''
					
				
			#print('FILE ' + filename + '... is in ...' + subfolder + ' in: ' + foldernames)

		
print('\nThere are ' + str(numFiles) + ' files in: ' + folder)
print('\nThere are ' + str(numFolders) + ' folders in: ' + folder)
print(f'\nTotal size of {folder} is {totalSize} bytes\n')
print(f'The folder that takes up the most disk space in {folder} is {largestFolder} bytes')

# TODO: • Walk a directory tree and archive just files with certain extensions, suchas .txt or .py, and nothing else 

# TODO: • Walk a directory tree and archive every file except the .txt and .py ones