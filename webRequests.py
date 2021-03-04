# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:28:52 2019

@author: HP PC
"""

import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')


#type(res) # This returns a Response object containing the response the web server gave for my request

try:
	res.raise_for_status() # Error checking
except Exception as exc:
	print('There was a problem: {}'.format(exc))
res.status_code == requests.codes.ok # You can tell if the request suceeded by checking the status_code attribute of the Response object. if it is equal to requests.codes.ok, then it was successful

len(res.text) # Returns the length of the text in the web page requested

print(res.text[:250])

playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
	playFile.write(chunk)
	
playFile.close()
'''The iter_content() method returns “chunks” of the content on each
iteration through the loop. Each chunk is of the bytes data type, and you
get to specify how many bytes each chunk will contain. One hundred
thousand bytes is generally a good size, so pass 100000 as the argument to
iter_content(). The file RomeoAndJuliet.txt will now exist in the current working directory. Note that while the filename on the website was pg1112.txt, the file on your hard drive has a different filename. The requests module simply handles downloading the contents of web pages. Once the page is downloaded, it is simply data in your program. Even if you were to lose your Internet connection after downloading the web page, all the page data would still be on your computer. The write() method returns the number of bytes written to the file. In the previous example, there were 100,000 bytes in the first chunk, and the remaining part of the file needed only 78,981 bytes.'''