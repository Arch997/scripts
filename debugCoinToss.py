# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:57:35 2019

Debugging Coin Toss
The following program is meant to be a simple coin toss guessing game. The
player gets two guesses (it’s an easy game). However, the program has several
bugs in it. Run through the program a few times to find the bugs that
keep the program from working correctly.

@author: HP PC
"""

import random, logging

logging.basicConfig(level = logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
	logging.debug('Start of coin toss')
	print('Guess the coin toss! Enter heads or tails:')
	guess = int(input())
	toss = random.randint(0, 1) # 0 is tails, 1 is heads
	if toss == guess:
		print('You got it!')
	else:
		print('Nope! Guess again!')
		guess = int(input())
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')
	#logging.debug('End of coin toss')
		
logging.debug('End of program')