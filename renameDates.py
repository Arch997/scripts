# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:37:42 2019

# Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

Say your boss emails you thousands of files with American-style dates
(MM-DD-YYYY) in their names and needs them renamed to European-style
dates (DD-MM-YYYY). This boring task could take all day to do by
hand! Let’s write a program to do it instead.
Here’s what the program does:
• It searches all the filenames in the current working directory for
American-style dates.
• When one is found, it renames the file with the month and day swapped
to make it European-style.
This means the code will need to do the following:
• Create a regex that can identify the text pattern of American-style dates.
• Call os.listdir() to find all the files in the working directory.
• Loop over each filename, using the regex to check whether it has a date.
• If it has a date, rename the file with shutil.move().
For this project, open a new file editor window and save your code as
renameDates.py.

1. Create Regex object to detect American-style dates(MM-DD-YYYY)
2. Get current working directory.
b. Call os.listdir() on all files in the working directory
c. iterate over each filename

3. Call the regex on all the filenames in cwd.
4. If Match object is found, swap the match with European-style dating(DD-MM-YYYY) using shutiil.move() 

@author: HP PC
"""
import re, os, shutil


datePattern = re.compile(r"""^(.*?) # all text before the date
((0|1)?\d)-          # one or two digits for the month
((0|1|2|3)?\d)-     # one or two digits for the day
((19|20)\d\d)      # four digits for the year
(.*?)$             # all text after the date
 """, re.VERBOSE)

path = 'C:\\delicious'
myDates = ['12-30-2019.txt', '02-12-1990.txt', '30-05-1990.dat', '11-24-1900.dat', '50-09-3000.dat', '09-09-2009']

'''for filename in myDates:
	path = os.path.join("C:\\delicious_backup", filename)
	print(path)
	pathFile = open(path, 'w')
	pathFile.write(filename)'''
	
#shutil.copy('C:\\delicious\\bacon.txt', 'C:\\delicious_backup')
	
for files in os.listdir('C:\\delicious_backup'):
	#print(files)
	#print(os.path.basename(files))
	if '-' not in files:
		#print(files)
		#print(os.path.basename(files))
		if 'bacon' not in files:
			print(files)
			os.unlink('C:\\delicious_backup\\%s' %(files))
	
	
# TODO: Loop over the files in the working directory.

for amerFilename in os.listdir('C:\\delicious_backup'):
	mo = datePattern.search(amerFilename)
# TODO: Skip files without a date
	if mo == None:
		continue
# TODO: Get the different parts of the filename.
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)
	print(mo.groups())
# TODO: Form the European-style filename.
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
# TODO: Get the full, absolute file paths.
	absWorkingDir = os.path.abspath('C:\\delicious_backup')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)
# TODO: Rename the files.
	print("Renaming file '%s' to '%s'..." % (amerFilename, euroFilename))
	shutil.move(amerFilename, euroFilename)
