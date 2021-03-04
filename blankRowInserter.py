# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:16:49 2019

Create a program blankRowInserter.py that takes two integers and a filename
string as command line arguments. Let’s call the first integer N and the second
integer M. Starting at row N, the program should insert M blank rows into the spreadsheet.

You can write this program by reading in the contents of the spreadsheet.
Then, when writing out the new spreadsheet, use a for loop to copy the first N lines. For the remaining lines, add M to the row number in the output spreadsheet.

@author: HP PC
"""

import openpyxl, os, sys, logging, traceback

os.chdir('C:\\Users\\HP PC\\Documents')


logging.basicConfig(level = logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


wb = openpyxl.load_workbook(sys.argv[3])
n = sys.argv[1]
m = sys.argv[2]
sheet = wb.active
sheet2 = wb.create_sheet(index=1, title='Sheet 2')
#sheet2 = wb['Second Sheet']

for rowOfCellObj in sheet['A1:D3']:
	for cellObj in rowOfCellObj:
		print(cellObj.coordinate, cellObj.value)
		sheet2['A1:D3'] = cellObj
#shwwt2.insert_row
	

