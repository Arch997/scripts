# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 21:38:08 2019

@author: HP PC
"""

import os, logging, PyPDF2

dictionary = open ('C:\\Users\\HP PC\\Desktop\\Py\\words1\\large', 'r')
flag = 0
words = []
pdfObj = open('C:\\Users\\HP PC\\Documents\\allminutes_encrypted.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfObj)
print(pdfReader.isEncrypted)


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s ')
logging.debug('Start of program')
for word in dictionary:
	words.append(word.strip('\n'))
	
logging.debug("Start of decryption: %%")
for word in words[124120:124300]:
	pdfReader.decrypt(word)
	logging.debug('Decrypting: %s%%' %(word))	
	if pdfReader.decrypt(word.upper()) or pdfReader.decrypt(word.lower()) == 1:
		print(f'Correct. Password is {word}')
		break
		
logging.debug("End of program")