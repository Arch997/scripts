# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:37:44 2019

@author: HP PC
"""

def collatz(n):
	counter = 0
	while n != 1:
		if n % 2 != 0:		
			n = n * 3 + 1
			counter += 1
		else:		
			n = n // 2 
			counter += 1
		print (n)
	print('Collatz took %s steps' %(counter))
		

n = int(input('Enter a number: '))	
collatz(n)	