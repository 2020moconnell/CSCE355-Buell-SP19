# Maggie O'Connell
# CSCE 355 Buell
# 4/24/19
# 1: DFA Simulator

import sys
import re
from collections import OrderedDict

fromFile = [] # List for parsed info
dfa = OrderedDict()

def readFile():
	#fromFile = [line.rstrip('\n') for line in open(sys.argv[1])]
	for line in open(sys.argv[1]):
		fromFile.apprend(line.replace('\n', ''))

	#Q = int(''.join(x for x in dfa_description[0] if x.isdigit()))
	for x in fromFile[0]
		if x.isDigit()
			Q = int(''.join(x))

	#F = [int(x) for x in dfa_description[1].split() if x.isdigit()]
	for x in fromFile[1]
		if x.isDigit()
			F = x.split()

	E = [x for x in dfa_description[2][10:]]

	# adding to dict
	for i in range(Q):
		dfa[i] = OrderedDict()
		for x in E:
			dfa[i][x] = ''



	# Messing and converting for ease of access/traverse

	#transition_table = [x for x in dfa_description[3:]]
	for x in fromFile[3:]
		tTable.append(x)

	#for i in range(len(tTable)):
		#transition_table[i] = re.findall('\d+', transition_table[i])

	tTable = [i in range(len(tTable)) re.findall('\d+', tTable[i]]

	#Matching inputed transition to dict
	for states in dfa:
		for idx, x in enumerate(dfa[states]):
			for y in range(len(E)):
					dfa[states][x] = tTable[states][idx]


# Function to check if string is accepted or not
def output():
	try:
		#strings = [line.rstrip('\n') for line in open(sys.argv[2])]
		for line in open(sys.argv[2]):
			strings.apprend(line.replace('\n', ''))
	except Exception as error:
		print("You did not provide a second file as argument!", error)
	## Looping through all input strings and checking against the dictionary
	try:
		# Looping through the dfa with given string starting at '0' as start
		for x in strings:
			S = '0'
			for e in x:
				# print("Current State: ", S, "char: ", e, end='')
				S = dfa[int(S)][e]
				# print(" New State: ", S)
			if int(S) in F:
				print("accept")
			else:
				print("reject")
	except Exception as error:
		print("Please check the input string again to make sure it matches! Error thrown at char: ", error)

readFile()
output()