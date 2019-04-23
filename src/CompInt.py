# Maggie O'Connell
# CSCE 355 Buell
# 4/24/19
# 2: Complement and Intersection

import sys
import re
from collections import OrderedDict

def run_script():
    if(len(sys.argv) == 2):
        comp()
    elif(len(sys.argv) == 3):
        inter()

# Complement DFA switches accepting and nonaccepting states
def comp():
    for line in open(sys.argv[1]):
		fromFile.append(line.replace('\n', ''))
    states = re.findall('\d+',fromFile[0])
    counter = int(states[0])
    accepting_states = re.findall('\d+',fromFile[1])
    for i in range(len(fromFile)):
        if(i == 1):
            print(fromFile[i][0:18],end = '')
            for i in range(counter):
                if(not str(i) in accepting_states):
                    print(i, "", end ='')
            print()
        else:
            print(fromFile[i])

def inter():
    #
    #dfa1 = [line.rstrip('\n') for line in open(sys.argv[1])]
    for line in open(sys.argv[1]):
		dfa1.append(line.replace('\n', ''))
    #dfa2 = [line.rstrip('\n') for line in open(sys.argv[2])]
    for line in open(sys.argv[2]):
		fromFile.append(line.replace('\n', ''))
    #dfa1_Q = int(''.join(x for x in dfa1[0] if x.isdigit()))
    for x in dfa1[0]:
	    if x.isDigit():
			dfa1_Q = int(''.join(x))
    #dfa2_Q = int(''.join(x for x in dfa2[0] if x.isdigit()))
    for x in fromFile[0]:
	    if x.isDigit():
			dfa2_Q = int(''.join(x))
    dfa1_accept = re.findall('\d+',dfa1[1])
    dfa2_accept = re.findall('\d+',dfa2[1])

    # Calculating num of states in final dfa
    numStates = dfa1_Q * dfa2_Q

    theStates = []
    for i in range(dfa1_Q):
        for j in range(dfa2_Q):
            theStates.append(str(i) +','+ str(j))

    accept_States = []
    for i in dfa1_accept:
        for j in dfa2_accept:
            accept_States.append(i +','+ j)
    iOfAccept = []
    for i in accept_States:
        iOfAccept.append(theStates.index(i))

    Alphabet = dfa1[2]
    E = [x for x in dfa1[2][10:]]



