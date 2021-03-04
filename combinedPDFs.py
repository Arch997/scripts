# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 06:12:08 2019

Say you have the boring job of merging several dozen PDF documents into
a single PDF file. Each of them has a cover sheet as the first page, but you
don’t want the cover sheet repeated in the final result. Even though there
are lots of free programs for combining PDFs, many of them simply merge
entire files together. Let’s write a Python program to customize which pages
you want in the combined PDF.
At a high level, here’s what the program will do:



In terms of implementation, your code will need to do the following:
• Call os.listdir() to find all the files in the working directory and
remove any non-PDF files.
• Call Python’s sort() list method to alphabetize the filenames.
• Create a PdfFileWriter object for the output PDF.
• Loop over each PDF file, creating a PdfFileReader object for it.
• Loop over each page (except the first) in each PDF file.
• Add the pages to the output PDF.
• Write the output PDF to a file named allminutes.pdf.

@author: HP PC
"""

import os, PyPDF2

# TODO: • Find all PDF files in the current working directory
cwd = os.chdir("C:\\Users\\HP PC\\Documents")
pdfList = []

for files in os.listdir(cwd):
	if files.endswith('.pdf'):
		pdfList.append(files)

# TODO: • Sort the filenames so the PDFs are added in order.
pdfList.sort(key=str.lower)

# TODO: • Write each page, excluding the first page, of each PDF to the output file.

pdfWriter = PyPDF2.PdfFileWriter()

for files in pdfList:
	pdfObj = open(files, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfObj)
	
for pageNum in range(1, pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)
	pdfWriter.addPage(pageObj)
	
resultPdf = open('allminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()

	

		
		
		
		
