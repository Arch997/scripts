# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:23:27 2019

Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string

@author: HP PC
"""

import re

def regex_strip(s, chars = None):
	if chars is None:
		strip_left = re.compile(r'^\s*')
		strip_right = re.compile(r'\s*')
	else:
		strip_left = re.compile(r'^[' + re.escape(chars) + r']*')
		strip_right = re.compile(r'[' + re.escape(chars) + r']*$')
		
	s = re.sub(strip_left, "", s)
	s = re.sub(strip_right, "", s)
	return s


string = ' Q h  Alphabeta metamorphosis completus fossilica. lorem ipsum cat \
photos of ginger.  '
st2 = 'Q molok ohgd   hkkhfd ,kjhbmnh jj nn *(*()  '
print(regex_strip(string))