# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:53:44 2019

Table Printer
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain this

@author: HP PC
"""
import pprint
tableData =  [['apples', 'cheese', 'macaroni', 'bacon'],
			  ['Alice', 'Bob', 'Carol', 'David'],
			  ['dog', 'mouse', 'cat', 'goose']]


#longest = max(tableData, key = len)
#print(longest[i])
	
#[[row[i] for row in tableData] for i in range(4)] List comprehension
#print(list(zip(*tableData))) Using zip() function to transpose the list

def printTable(table, colWidths):
	colWidths = [0] * len(tableData)
	for n in range(1):
		print(table[0][0].rjust(12),table[1][0].rjust(12), table[2][0].rjust(12), end='')
		print()
		
		for o in range(1):
			print(table[0][1].rjust(12), table[1][1].rjust(12), table[2][1].rjust(12), end='')
			print()
			for p in range(1):
				print(table[0][2].rjust(12), table[1][2].rjust(12), table[2][2].rjust(12), end='')
				print()
				for q in range(1):
					print(table[0][3].rjust(12), table[1][3].rjust(12), table[2][3].rjust(12), end='')
					print()


	'''for i in range():	
		#print(str(i).rjust(8))		
		longest = max(tableData[0:2], key = len)
		counter = len(longest)
		colWidths0 = 8
		text = '\n'.join(tableData[0:2][0:])
		print(i.rjust(colWidths0) + a.rjust(colWidths1))
		for j in range(1):
			longest = max(tableData[1][0:3], key = len)
			counter = len(longest)
			colWidths1 = 5
			text = '\n'.join(tableData[1][0:])
			lines = text.split('\n')
			print()
			for k in range(1):
				longest = max(tableData[2][0:3], key = len)
				counter = len(longest)
				colWidths[2] = 5
				print(longest)'''
							
printTable(tableData, 16)
