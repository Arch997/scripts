# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:55:27 2019

@author: HP PC
"""

import re

pos = ['ADJECTIVE', "NOUN", "VERB", "NOUN"]

replacements = {_:'' for _ in pos}
for r in replacements:
	replacements[r] = input('Enter a ' + r.lower() + ': ')
	
madLibs = ["The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events"]

def replace(mo):
	content = mo.group()
	if content in pos:
		return replacements[content] 
	else:
		return content
	
for madLib in madLibs:
	result = re.sub(r'[A-Z]+', replace, madLib)
	print(result)

madLibFile = open('madLib.txt', 'w')
madLibFile.write(result)
madLibFile.close()


		

