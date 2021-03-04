# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:21:06 2019
#! python3
Blogs and other regularly updating websites usually have a front page with
the most recent post as well as a Previous button on the page that takes you
to the previous post. Then that post will also have a Previous button, and so
on, creating a trail from the most recent page to the first post on the site.
If you wanted a copy of the site’s content to read when you’re not online,
you could manually navigate over every page and save each one. But this is
pretty boring work, so let’s write a program to do it instead. XKCD is a popular geek webcomic with a website that fits this structure (see Figure 11-6). The front page at http://xkcd.com/ has a Prev button that guides the user back through prior comics. Downloading each comic by hand would take forever, but you can write a script to do this in a couple of minutes.
Here’s what your program does:
• Loads the XKCD home page.
• Saves the comic image on that page.
• Follows the Previous Comic link.
• Repeats until it reaches the first comic.

This means your code will need to do the following:
• Download pages with the requests module.
• Find the URL of the comic image for a page using Beautiful Soup.
• Download and save the comic image to the hard drive with iter_content().
• Find the URL of the Previous Comic link, and repeat.

Step 1: Design the Program
If you open the browser’s developer tools and inspect the elements on the
page, you’ll find the following:
• The URL of the comic’s image file is given by the href attribute of an
<img> element.
• The <img> element is inside a <div id="comic"> element.
• The Prev button has a rel HTML attribute with the value prev.
• The first comic’s Prev button links to the http://xkcd.com/# URL, indicating
that there are no more previous pages.

@author: HP PC
"""

import requests, os, bs4

url = 'http://www.xkcd.com'
os.makedirs('xkcd', exist_ok = True)

while not url.endswith("#"):
   # TODO: Download the page.
   print('Downloading page{}...'.format(url))
   res = requests.get(url)
   print(res.raise_for_status())
   soup = bs4.BeautifulSoup(res.text, features='lxml')
   
   # TODO: Find the URL of the comic image.
   comicElem = soup.select('#comic img')
   if comicElem == []:
	   print('Could not find comic image')
   else:
	   comicUrl = comicElem[0].get('src')
# TODO: Download the image.
   print('Downloading image %s...' % (comicUrl))
   res = requests.get(comicUrl)
   print(res.raise_for_status())
# TODO: Save the image to ./xkcd.
   imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
   for chunk in res.iter_content(100000):
	   imageFile.write(chunk)
   imageFile.close()
# TODO: Get the Prev button's url.\
   prevLink = soup.select('a[rel="prev"]')[0]
   url = 'http://xkcd.com' + prevLink.get('href')
   
print('Done')  

'''
You’ll have a url variable that starts with the value 'http://xkcd.com'
and repeatedly update it (in a for loop) with the URL of the current page’s
Prev link. At every step in the loop, you’ll download the comic at url. You’ll know to end the loop when url ends with '#'. You will download the image files to a folder in the current working directory named xkcd. The call os.makedirs() ensures that this folder exists, and the exist_ok=True keyword argument prevents the function from throwing an exception if this folder already exists. The rest of the code is just comments that outline the rest of your program. First, print url so that the user knows which URL the program is about to download; then use the requests module’s request.get() function to download it. As always, you immediately call the Response object’s raise_for_status() method to throw an exception and end the program if something went wrong with the download. Otherwise, you create a BeautifulSoup object from the text of the downloaded page. From inspecting the XKCD home page with your developer tools, you know that the <img> element for the comic image is inside a <div> element with the id attribute set to comic, so the selector '#comic img' will get you the correct <img> element from the BeautifulSoup object. A few XKCD pages have special content that isn’t a simple image file. That’s fine; you’ll just skip those. If your selector doesn’t find any elements, then soup.select('#comic img') will return a blank list. When that happens, the program can just print an error message and move on without downloading the image. Otherwise, the selector will return a list containing one <img> element. You can get the src attribute from this <img> element and pass it to requests.get() to download the comic’s image file.
At this point, the image file of the comic is stored in the res variable.
You need to write this image data to a file on the hard drive. You’ll need a filename for the local image file to pass to open(). The comicUrl will have a value like 'http://imgs.xkcd.com/comics/heartbleed _explanation.png'—which you might have noticed looks a lot like a file path. And in fact, you can call os.path.basename() with comicUrl, and it will return just the last part of the URL, 'heartbleed_explanation.png'. You can use this as the filename when saving the image to your hard drive. You join this name with the name of your xkcd folder using os.path.join() so that your program uses backslashes (\) on Windows and forward slashes (/) on OS X and Linux. Now that you finally have the filename, you can call open() to open a new file in 'wb' “write binary” mode. Remember from earlier in this chapter that to save files you’ve downloaded using Requests, you need to loop over the return value of the iter_content() method. The code in the for loop writes out chunks of the image data (at most 100,000 bytes each) to the file and then you close the file. The image is now saved to your hard drive. Afterward, the selector 'a[rel="prev"]' identifies the <a> element with the rel attribute set to prev, and you can use this <a> element’s href attribute to get the previous comic’s URL, which gets stored in url. Then the while loop begins the entire download process again for this comic.

Ideas for Similar Programs
Downloading pages and following links are the basis of many web crawling
programs. Similar programs could also do the following:
• Back up an entire site by following all of its links.
• Copy all the messages off a web forum.
• Duplicate the catalog of items for sale on an online store.
'''
