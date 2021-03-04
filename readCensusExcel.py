# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:46:37 2019

Say you have a spreadsheet of data from the 2010 US Census and you
have the boring task of going through its thousands of rows to count both
the total population and the number of census tracts for each county. (A
census tract is simply a geographic area defined for the purposes of the
census.). Each row represents a single census tract.

Even though Excel can calculate the sum of multiple selected cells,
you’d still have to select the cells for each of the 3,000-plus counties. Even
if it takes just a few seconds to calculate a county’s population by hand,
this would take hours to do for the whole spreadsheet.
In this project, you’ll write a script that can read from the census spreadsheet file and calculate statistics for each county in a matter of seconds.
This is what your program does:
• Reads the data from the Excel spreadsheet.
• Counts the number of census tracts in each county.
• Counts the total population of each county.
• Prints the results.
This means your code will need to do the following:
• Open and read the cells of an Excel document with the openpyxl module.
• Calculate all the tract and population data and store it in a data structure.
• Write the data structure to a text file with the .py extension using the
pprint module.
																	   
@author: HP PC
"""

import openpyxl, os, pprint

os.chdir('C:\\Users\\HP PC\\Downloads')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

# TODO: Fill in countyData with each county's population and tracts.
for row in range(2, sheet.max_row + 1):
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value
#Make sure the key for this state exists.	
	countyData.setdefault(state, {})
# Make sure the key for this county in state exists
	countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
## Each row represents one census tract, so increment by one.
	countyData[state][county]['tracts']+=1
# Increase the county pop by the pop in this census tract
	countyData[state][county]['pop']+= int(pop)
	
# Open a new tect file and write the contents of countyData to it
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')
'''
Step 2: Populate the Data Structure
The data structure stored in countyData will be a dictionary with state abbreviationsas its keys. Each state abbreviation will map to another dictionary, whose keys are strings of the county names in that state. Each county name will in turn map to a dictionary with just two keys, 'tracts' and 'pop'. These keys map to the number of census tracts and population for the county. For example, the dictionary will look similar to this:
{'AK': {'Aleutians East': {'pop': 3141, 'tracts': 1},
'Aleutians West': {'pop': 5561, 'tracts': 2},
'Anchorage': {'pop': 291826, 'tracts': 55},
'Bethel': {'pop': 17013, 'tracts': 3},
'Bristol Bay': {'pop': 997, 'tracts': 1},
--snip--
If the previous dictionary were stored in countyData, the following
expressions would evaluate like this:
>>> countyData['AK']['Anchorage']['pop']
291826
>>> countyData['AK']['Anchorage']['tracts']
55
More generally, the countyData dictionary’s keys will look like this:
countyData[state abbrev][county]['tracts']
countyData[state abbrev][county]['pop']
'''	

	
	