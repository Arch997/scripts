# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:45:05 2019

Strong Password Detection
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength.

@author: HP PC
"""
import re

#pwRegex = re.compile(r'[(A-Z)0-9(a-z)]{8}')
mo = ['123456789', 'aaAAA122', '123sdGH', '123sdGHI', '123sdGHIJK', 'aaaaaaaa', 'BBBBB1']
pwRegex = re.compile(r'\d.*?[A-Z].*?[a-z]')
if pwRegex.match(''.join(sorted(mo))) and len(mo) >= 8:
	print ("OK")
mo = pwRegex.findall('123456789 AAA122 123sdGH 123sdGHI 123sdGHIJK aaaaaaaa BBBBB1 aaaaa123456')
print(mo)

	
'''def pw(text):
	if (any(i.isupper() for i in text) and any(i.islower() for i in text) and any(i.isdecimal() for i in text) and len(text) >= 8):
		return True
	
while True:
	password = input('Enter a password: ')
	pw(password)
	if not len(password) >= 8:
		print('Password should be at least 8 characters')
		continue
	if not any(x.isupper() for x in password):
		print("Your password should have at least one uppercase")
		continue
	if not any(x.islower() for x in password):
		print('No lowercase')
		continue
	if not any(x.isdecimal() for x in password):
		print('No numerix characters')
		continue
	else:
		break'''

	