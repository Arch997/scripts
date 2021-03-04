# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:27:07 2020

@author: HP PC
"""

from threading import Thread
from time import time, sleep

print("Start of program")
def takeNap():
	sleep(5)
	print('Wake up!')
	
threadObj = Thread(target=takeNap)
threadObj.start()

print('End of program')

#print('Cats', 'Dogs', "Frogs", sep=' & ')

threadObj = Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()

"""
To make sure the arguments 'Cats', 'Dogs', and 'Frogs' get passed to print() in the new thread, we pass args=['Cats', 'Dogs', 'Frogs'] to threading. Thread(). To make sure the keyword argument sep=' & ' gets passed to print() in the new thread, we pass kwargs={'sep': '& '} to threading.Thread(). The threadObj.start() call will create a new thread to call the print() function, and it will pass 'Cats', 'Dogs', and 'Frogs' as arguments and ' & ' for the sep keyword argument. This is an incorrect way to create the new thread that calls print(): threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & ')) What this ends up doing is calling the print() function and passing its return value (print()’s return value is always None) as the target keyword argument. It doesn’t pass the print() function itself. When passing arguments to a function in a new thread, use the threading.Thread() function’s args and kwargs keyword arguments."""


