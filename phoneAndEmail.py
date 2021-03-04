# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:25:34 2019

@author: HP PC
"""

import re, pyperclip

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?             # area code
(\s|-|\.)?                     # separator
(\d{3})                        # first 3 digits
(\s|-|\.)                      # separator
(\d{4})                        # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

# TODO: Create email regex.
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+    #username
@                    #@ symbol
[a-zA-Z0-9.-]+       #domain name
(\.[a-zA-Z]{2,4})	 #dot-something
)''', re.VERBOSE)
# TODO: Find matches in clipboard text.

text= str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
		matches.append(phoneNum)
		
for groups in emailRegex.findall(text):
	matches.append(groups[0])
# TODO: Copy results to the clipboard.
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')
	
someRegex = re.compile(r'(\d{1,},\d{3})+')
mo = someRegex.findall('12,233,444 1,2,23 1,222,444,444 1,22,222. i\'m a teapot')
print(mo)

nameRegex = re.compile(r'[A-Z][a-z]*\sNakamoto')
mo = nameRegex.findall('Satoshi nakamoto Satoshi Nakamoto Robocop Nakamoto satoshi Nakamoto.SSatoshi Nakamoto i\'m a teapot')
print(mo)

'''
How would you write a regex that matches a sentence where the first
word is either Alice, Bob, or Carol; the second word is either eats, pets, or
throws; the third word is apples, cats, or baseballs; and the sentence ends
with a period? This regex should be case-insensitive. It must match the
following:
• 'Alice eats apples.'
• 'Bob pets cats.'
• 'Carol throws baseballs.'
• 'Alice throws Apples.'
• 'BOB EATS CATS.'
but not the following:
• 'RoboCop eats apples.'
• 'ALICE THROWS FOOTBALLS.'
• 'Carol eats 7 cats.' '''

sentRegex = re.compile(r'[Alice|Bob|Carol]+\s[eats|pets|throws]+\s[apples|cats|baseballs]+\.', re.I)
mo = sentRegex.findall('Alice eats apples. Bob pets cats. carol throws baseballs. Alice throws Apples. BOB EATS CATS. RoboCop eats apples. ALICE THROWS FOOTBALLS. Carol eats 7 cats.')
print(mo)
