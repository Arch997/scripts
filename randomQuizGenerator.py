# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:31:58 2019

'''• Creates 35 different quizzes.
• Creates 50 multiple-choice questions for each quiz, in random order.
• Provides the correct answer and three random wrong answers for each
question, in random order.
• Writes the quizzes to 35 text files.
• Writes the answer keys to 35 text files.
This means the code will need to do the following:
• Store the states and their capitals in a dictionary.
• Call open(), write(), and close() for the quiz and answer key text files.
• Use random.shuffle() to randomize the order of the questions and
multiple-
choice options.

@author: HP PC
"""
#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming':'Cheyenne'}
# Generate 35 quiz files.
for quizNum in range(35):
	# TODO: Create the quiz and answer key files.
	quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
# TODO: Write out the header for the quiz.
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + "State Capital's Quiz(Form %s)" % (quizNum + 1))
	quizFile.write('\n\n')	
# TODO: Shuffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)	
# TODO: Loop through all 50 states, making a question for each
	
for questionNum in range(50):
	correctAnswer = capitals[states[questionNum]]
	wrongAnswers = list(capitals.values())
	del wrongAnswers[wrongAnswers.index(correctAnswer)]
	wrongAnswers = random.sample(wrongAnswers, 3)
	print(wrongAnswers)
	answerOptions = wrongAnswers + [correctAnswer]
	print(answerOptions)
	random.shuffle(answerOptions)
# TODO: Write the question and answer options to the quiz file.	
	quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
'''
The correct answer is easy to get — it’s stored as a value in the capitals
dictionary. This loop will loop through the states in the shuffled states
list, from states[0] to states[49], find each state in capitals, and store that state’s corresponding capital in correctAnswer.
The list of possible wrong answers is trickier. You can get it by duplicating all the values in the capitals dictionary, deleting the correct answer, and selecting three random values from this list. The random.sample() function makes it easy to do this selection. Its first argument is the list you want to select from; the second argument is the number of values you want to select. The full list of answer options is the combination of these three wrong answers with the correct answers. Finally, the answers need to be randomized so that the correct response isn’t always choice D.
'''
# TODO: Write the answer key to a file.  
for i in range(4):
	quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
quizFile.write('\n')
answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()	

'''
A for loop that goes through integers 0 to 3 will write the answer options
in the answerOptions list. The expression 'ABCD'[i] treats the string
'ABCD' as an array and will evaluate to 'A','B', 'C', and then 'D' on each
respective iteration through the loop.
In the final line, the expression answerOptions.index(correctAnswer)
will find the integer index of the correct answer in the randomly ordered
answer options, and 'ABCD'[answerOptions.index(correctAnswer)] will evaluate
to the correct answer’s letter to be written to the answer key file.
After you run the program, this is how your capitalsquiz1.txt file will
look, though of course your questions and answer options may be different
from those shown here, depending on the outcome of your random.shuffle()
calls
'''
	