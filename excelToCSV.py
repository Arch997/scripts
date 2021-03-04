# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 08:51:30 2019

Excel can save a spreadsheet to a CSV file with a few mouse clicks, but if you
had to convert hundreds of Excel files to CSVs, it would take hours of clicking.
Using the openpyxl module from Chapter 12, write a program that reads
all the Excel files in the current working directory and outputs them as CSV
files. A single Excel file might contain multiple sheets; you’ll have to create
one CSV file per sheet. The filenames of the CSV files should be <excel
filename>_<sheet title>.csv, where <excel filename> is the filename of the Excel
file without the file extension (for example, 'spam_data', not 'spam_data.xlsx')
and <sheet title> is the string from the Worksheet object’s title variable.
This program will involve many nested for loops. The skeleton of the
program will look something like this:
for excelFile in os.listdir('.'):
# Skip non-xlsx files, load the workbook object.
for sheetName in wb.get_sheet_names():
# Loop through every sheet in the workbook.
sheet = wb.get_sheet_by_name(sheetName)
# Create the CSV filename from the Excel filename and sheet title.
# Create the csv.writer object for this CSV file.
# Loop through every row in the sheet.
for rowNum in range(1, sheet.get_highest_row() + 1):
rowData = [] # append each cell to this list
# Loop through each cell in the row.
for colNum in range(1, sheet.get_highest_column() + 1):
# Append each cell's data to rowData.
# Write the rowData list to the CSV file.
csvFile.close()

@author: HP PC
"""

import csv, openpyxl, os, logging

cwd = os.chdir('C:\\Users\\HP PC\\Downloads')
files = []
rowData = []

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s ')
logging.debug('Start of program: %%')

for file in os.listdir(cwd):
	
	if file.endswith('.xlsx'):
		logging.debug('Reading Excel Files: %s%%' %(file))
		try:
			wb = openpyxl.load_workbook(file)
			for sheetName in wb.sheetnames:
				sheet = wb[sheetName]
				
				csvFile = open(file.rstrip('.xlsx') + "_" + sheet.title + '.tsv', 'w', newline='')
				writer = csv.writer(csvFile, delimiter='\n', lineterminator='\n\n')
				files.append(file)
				
				#for row in range(1, sheet.max_row + 1):
				for rows in sheet.iter_rows(min_row=1, values_only=True):	
					rowData.append(rows)	
					#print(cols)				
										
		#'''for column in range(1, sheet.max_column + 1):
			#for colOfCellObj in sheet[column]:
				#rowData.append(colOfCellObj.value)'''		
				   					
					logging.debug('Writing to CSV: %s %s%%' %(file, csvFile))
					writer.writerow([rows])
				csvFile.close()			

		except:
			continue
		
			#print(sheet)
		

