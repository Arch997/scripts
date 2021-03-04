# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 09:28:16 2020

@author: HP PC
"""

from time import time, sleep

input() # Press Enter to begin
print('Started...')

now = time()
startTime = time()
lastTime = startTime
endTime = time()
print(now)

lapCtr = 1

while True:
	try:
		input()
		lapTime = round(time() - lastTime, 2)
		totalTime = round(time() - startTime, 2)
		print('Lap #%s: %s(%s)' %(lapCtr, totalTime, lapTime), end='')
		lapCtr += 1
		lastTime = time() # Reset the last tap time
		
	except KeyboardInterrupt:
		print('\nDone')
		