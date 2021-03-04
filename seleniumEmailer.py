# -*- coding: utf-8 -*-
"""
#! python3

Command Line Emailer
Write a program that takes an email address and string of text on the command
line and then, using Selenium, logs into your email account and
sends an email of the string to the provided address. (You might want to set
up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from a Facebook
or Twitter account.

1. Request for input from user containing email address and string of text
2. Pass input to sys.argv[1:]
3. Pass sys.argv[1] to 'email' variable
4. Open browser with webdriver. 
5. Direct browser to gmail URL
6. Using find_element_by_id(), pass the email and password attribute values to different variables.
7. Using send_keys(), send them to the text fields 
8. Submit
9. Join sys.argv[2:] to form a string. Save it to a variable
10. Look through the developer tools for the element that represents the send new mail option. Or use requests, download the HTML of that file, and search for the element. 
a. Do the same for the message recipient element

11. Pass the element to find_element* and save in a variable
12. Assign the variable send.keys() method. Pass the text var to send.keys(*text) as an argument so it sends as an email
13. Repeat step 11 for msgElem var
14. Repeat step 12 for recipientElem var. Pass email var*(sys.argv[1]) to send.keys() as arg
15. Submit
 
Created on Thu Nov 28 21:34:40 2019


@author: HP PC
"""
import sys, bs4
from selenium import webdriver

full = input("Enter recipient email address: \nEnter message")
sys.argv[1:] = full

address = sys.argv[1]
text = ' '.join(sys.argv[2:])

browser = webdriver.Firefox()
browser.get('https://gmail.com')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('outlooknga@gmail.com')
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('b33tl3jnlc3')
passwordElem.submit()






