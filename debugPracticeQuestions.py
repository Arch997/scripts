# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 10:57:38 2019

@author: HP PC
"""

'''
Write an assert statement that triggers an AssertionError if the variables
eggs and bacon contain strings that are the same as each other, even if
their cases are different (that is, 'hello' and 'hello' are considered the
same, and 'goodbye' and 'GOODbye' are also considered the same).
'''

bacon = 'goodBye'
eggs = 'goodbye'

assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same' #or assert(eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same') 
assert False, 'AssertionError is set to always True'

   
   