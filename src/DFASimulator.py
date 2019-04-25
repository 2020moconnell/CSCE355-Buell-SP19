# Maggie O'Connell
# CSCE 355 Buell
# 4/24/19
# 1: DFA Simulator

import sys
import re
from collections import OrderedDict
DFAinfo = []
dfa = OrderedDict()
tempList1 = []
tempList2 = []
TTable = []
F = []
Q = []
E = []

def dfaDescription():
	global F
	for line in open(sys.argv[1]):
		DFAinfo.append(line.replace('\n',''))

	for x in DFAinfo[0]:
		if x.isdigit():
			tempList1.append(x)
	Q = int(''.join(tempList1))

	for x in DFAinfo[1].split():
		if x.isdigit():
			F.append(int(x))

	for x in DFAinfo[2][10:]:
		E.append(x)
######################################################################### sec 1

	h = 0
	while h < Q:
		dfa[h] = OrderedDict()
		for x in E:
			dfa[h][x] = ''
		h += 1

	# Messing and converting for ease of access/traverse
	for x in DFAinfo[3:]:
		TTable.append(x)


	for i in range(len(TTable)):
		TTable[i] = re.findall('\d+', TTable[i])
	#Matching inputed transition to dict
	for states in dfa:
		for idx, x in enumerate(dfa[states]):
			for y in range(len(E)):
					dfa[states][x] = TTable[states][idx]
# Function to check if string is accepted or not
def output():
	try:
		strings = [line.rstrip('\n') for line in open(sys.argv[2])]
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

dfaDescription()
output()