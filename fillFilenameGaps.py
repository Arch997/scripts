# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:28:18 2019

Filling in the Gaps
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added

# Regex,
1. Import re, os, shutil
2. Get working directory
3. List the contents of the folder.
a. For filenames with numbers, iterate over os.listdir(folder)
b. Assign basename of files to var iteratively
c. (i) Check if there's a module or function to enable checks if filenames are organised serially for filenames in folder. If so, use this function
    (ii). Else, use conditional statements to solve this problem.
d. If the filenames are organized serially, print Notif message, break.
   (ii) Else, rename the files serially using shutil, flag variable which will increment with every iteration of the loop and placeholders to represent this flag and its incrementation.
e. Print messages in between each line of significant code to monitor the workings of the program

@author: HP PC
"""
import os, shutil, re


cwd = os.getcwd() # Get working directory

# Using list comprehension to access the files in cwd. The conditional statement in the list comprehensionm specifies that only files with numbers in them should be assigned
'''files = [filename for filename in os.listdir(cwd) if(any(filename.isdecimal() for filename in filename) and filename.startswith('delicious'))]
print(files)

ext = [files[-4:] for files in files]
number = [int(filename.lstrip('delicious_').rstrip(str(ext))) for filename in files]

print(number)
print(ext)

newFilenames = [str('delicious{:0>3}%s' %(ext).format(number + 1) for number in range(len(files)))]

for oldname, newname in zip(files, newFilenames):
    print(oldname)
    print(newname)
    os.rename(oldname, newname)'''


cwd = os.getcwd()
fileNum = 0
def fillGaps(folder, prefix):
    ext = ''
    fileRegex = re.compile(r'(%s)(\d)+\.%s' % (prefix, ext))
    matchlist = []
    folder = os.path.abspath(folder)
    os.chdir(folder)

    for filename in os.listdir(folder):
        mo = fileRegex.match(filename)
        if mo:
            matchlist.append(filename)
            if int(mo.group(2) == len(matchlist)):
                continue
            else:
                print(filename + ' is the ' + str(len(matchlist)) + 'th file')
                if len(matchlist) < 9:
                    print (filename +' will be renamed: ' + prefix + '00' + str(len(matchlist)) + ext)
                    newname = prefix + '00' + str(len(matchlist)) + ext
                    oldname = os.path.join(folder, filename)
                    newname = os.path.join(folder, newname)
                    #print(newname)
                elif 10 <= len(matchlist) < 100:
                    print(filename + ' will be renamed: ' + prefix + '0' + str(len(matchlist)) + ext)
                    newname = prefix + '0' + str(len(matchlist)) + ext
                    oldname = os.path.join(folder, filename)
                    newname = os.path.join(folder, newname)
                    print(newname)

    #print(filenames)
    '''if (any(filename.isdecimal() for filename in filenames)):
        #print(os.path.abspath(filenames))
        basenames = os.path.basename(filenames)
        fileNum += 1
        print(basenames + ': ' + str(fileNum))'''

fillGaps('C:\\Users\\HP PC\\practice projects', 'delicious_')

