# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:26:38 2019

Say you’re working on a project whose files you keep in a folder named
C:\AlsPythonBook. You’re worried about losing your work, so you’d like
to create ZIP file “snapshots” of the entire folder. You’d like to keep different versions, so you want the ZIP file’s filename to increment each
time it is made; for example, AlsPythonBook_1.zip, AlsPythonBook_2.zip. AlsPythonBook_3.zip, and so on. You could do this by hand, but it is rather
annoying, and you might accidentally misnumber the ZIP files’ names. It
would be much simpler to run a program that does this boring task for you.
For this project, open a new file editor window and save it as
backupToZip.py.
Step 1: Figure Out the ZIP File’s Name
The code for this program will be placed into a function named backupToZip().
This will make it easy to copy and paste the function into other Python programs that need this functionality. At the end of the program, the function
will be called to perform the backup.

#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

@author: HP PC
"""
import zipfile, os

def backupToZip(folder):
	#Backup the entire contents of folder into a ZIP file
	folder = os.path.abspath(folder) # Make sure the folder is absolute path
	#Figure out the filenames this code should use based on what files already exist
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number = number + 1
		# TODO: Create the ZIP file.
	print('Creating ZIP file %s' %(zipFilename))		
	backupZip = zipfile.ZipFile(zipFilename, 'w')
	
	#TOdo: Walk the entire folder tree and compress the files in each folder
	for foldername, subfolders, filenames in os.walk(folder):
		#Add files in the current foldername
		print('Adding files in %s...' %(foldername))
		backupZip.write(foldername)
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue # don't backup the backup ZIP files
			backupZip.write(os.path.join(foldername, filename))
		backupZip.close()
		print('Done.')	
		
backupToZip('C:\\delicious')

'''
Define a backupToZip() function that takes just one parameter, folder.
This parameter is a string path to the folder whose contents should be backed
up. The function will determine what filename to use for the ZIP file it will
create; then the function will create the file, walk the folder folder, and add
each of the subfolders and files to the ZIP file. Write TODO comments for these
steps in the source code to remind yourself to do them later x.
The first part, naming the ZIP file, uses the base name of the absolute
path of folder. If the folder being backed up is C:\delicious, the ZIP file’s
name should be delicious_N.zip, where N = 1 is the first time you run the program,
N = 2 is the second time, and so on.
Organizing Files 211
You can determine what N should be by checking whether delicious_1.zip
already exists, then checking whether delicious_2.zip already exists, and so
on. Use a variable named number for N v, and keep incrementing it inside
the loop that calls os.path.exists() to check whether the file exists w. The
first nonexistent filename found will cause

Ideas for Similar Programs
You can walk a directory tree and add files to compressed ZIP archives in
several other programs. For example, you can write programs that do the
following:
• Walk a directory tree and archive just files with certain extensions, such
as .txt or .py, and nothing else
• Walk a directory tree and archive every file except the .txt and .py ones
• Find the folder in a directory tree that has the greatest number of files
or the folder that uses the most disk space'''

				
