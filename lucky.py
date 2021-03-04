# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 00:54:24 2019

@author: HP PC
"""

import requests, sys, bs4, webbrowser

print('Googling...')
res = requests.get('http://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
print(res.raise_for_status())

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features ='lxml')

# TODO: Open a browser tab for each result.
linkElems = soup.select('.r a')
'''
If you look up a little from the <a> element, though, there is an element
like this: <h3 class="r">. Looking through the rest of the HTML source,
it looks like the r class is used only for search result links. You don’t have
to know what the CSS class r is or what it does. You’re just going to use
it as a marker for the <a> element you are looking for. You can create a
BeautifulSoup object from the downloaded page’s HTML text and then use
the selector '.r a' to find all <a> elements that are within an element that
has the r CSS class.'''

numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))
'''
By default, you open the first five search results in new tabs using the
webbrowser module. However, the user may have searched for something that
turned up fewer than five results. The soup.select() call returns a list of all the elements that matched your '.r a' selector, so the number of tabs you want to open is either 5 or the length of this list (whichever is smaller). The built-in Python function min() returns the smallest of the integer or float arguments it is passed. (There is also a built-in max() function that returns the largest argument it is passed.) You can use min() to find out whether there are fewer than five links in the list and store the number of links to open in a variable named numOpen. Then you can run through a for loop by calling range(numOpen). On each iteration of the loop, you use webbrowser.open() to open a new tab in the web browser. Note that the href attribute’s value in the returned <a> elements do not have the initial http://google.com part, so you have to concatenate that to the href attribute’s string value.'''
