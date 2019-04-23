# Maggie O'Connell
# CSCE 355 Buell
# 4/24/19
# 2: Complement and Intersection

import sys
import re
from collections import OrderedDict
DFAinfo = []
dfa1 = []
dfa2 = []
tempList1 = []
tempList2 = []
dfa1_Q = []
dfa2_Q = []
E = []

def run_script():
   if(len(sys.argv) == 2):
      getComplement()
   elif(len(sys.argv) == 3):
      productConstruction()

## To Get Complement of DFA, you just swap accepting states with NON Accepting States
## So now non-accepting states are now accepting and accepting states are non-accepting
def getComplement():
   for line in open(sys.argv[1]):
      DFAinfo.append(line.replace('\n',''))
   states = re.findall('\d+',DFAinfo[0])
   counter = int(states[0])
   accepting_states = re.findall('\d+',DFAinfo[1])
   
   a = 0
   b = len(DFAinfo)
   d = 0
   c = counter
   while a < b:
	   if(a == 1):
		   print(DFAinfo[a][0:18], end = '')
		   while d < c:
			   if(not str(d) in accepting_states):
				   print(d, "", end = '')
			   d += 1
		   print()
		   a += 1
	   else:
		   print(DFAinfo[a])
		   a += 1


## This is finding the intersection between the two
## We will assume that it follows the format 0 = 00, 1 = 01 as in the first state of DFA A x(Cross Product) of DFA B will give us State 0. And it will continue...
def productConstruction():
   # Reading in files
   #dfa1 = [line.rstrip('\n') for line in open(sys.argv[1])]
   for line in open(sys.argv[1]):
      dfa1.append(line.replace('\n',''))
   #dfa2 = [line.rstrip('\n') for line in open(sys.argv[2])]
   for line in open(sys.argv[2]):
      dfa2.append(line.replace('\n',''))
   #dfa1_Q = int(''.join(x for x in dfa1[0] if x.isdigit()))
   for x in dfa1[0]:
     if x.isdigit():
       tempList1.append(x)
   dfa1_Q = int(''.join(tempList1))
   #dfa2_Q = int(''.join(x for x in dfa2[0] if x.isdigit()))
   for x in dfa2[0]:
     if x.isdigit():
       tempList2.append(x)
   dfa2_Q = int(''.join(tempList2))

   dfa1_accept = re.findall('\d+',dfa1[1])
   dfa2_accept = re.findall('\d+',dfa2[1])

   # Multiplying to get total states
   total_States = dfa1_Q * dfa2_Q # Using as Output for total of States
   # Getting combinations/permutations for each states
   theStates = []

   #e = 0
   #f = 0
   #while e < dfa1_Q:
#	   while f < dfa2_Q:
	#	   theStates.append(str(e) +','+ str(f))
	#	   f += 1
	 #  e += 1

   for i in range(dfa1_Q):
      for j in range(dfa2_Q):
         theStates.append(str(i) +','+ str(j)) ## EACH new state will be separated with comma, Ran into problem where we had 110 and 110 but different 1,10 and 11,0
   #Doing below for accepting States
   
   accept_States = []
   for i in dfa1_accept:
      for j in dfa2_accept:
         accept_States.append(i +','+ j)
   iOfAccept = [] # This is index of the accepting States.. Using this for output
   for i in accept_States:
      iOfAccept.append(theStates.index(i))

   Alphabet = dfa1[2] #Using this for Alphabet
   #E = [x for x in dfa1[2][10:]]
   for x in dfa1[2][10:]:
	   E.append(x)
   ## DFA 1
   dfa_table = OrderedDict()

   g = 0
   while g < dfa1_Q:
	   dfa_table[g] = OrderedDict()
	   for x in E:
		   dfa_table[g][x] = ''

   #for i in range(dfa1_Q):
   #   dfa_table[i] = OrderedDict()
   #   for x in E:
   #      dfa_table[i][x] = ''



   # Messing and converting for ease of access/traverse
   transition_table = [x for x in dfa1[3:]]
   for i in range(len(transition_table)):
      transition_table[i] = re.findall('\d+', transition_table[i])
   for states in dfa_table:
      for idx, x in enumerate(dfa_table[states]):
         for y in range(len(E)):
            dfa_table[states][x] = transition_table[states][idx]

   # DFA 2
   dfa2_table = OrderedDict()
   for i in range(dfa2_Q):
      dfa2_table[i] = OrderedDict()
      for x in E:
         dfa2_table[i][x] = ''
   transition_table2 = [x for x in dfa2[3:]]
   for i in range(len(transition_table2)):
      transition_table2[i] = re.findall('\d+', transition_table2[i])

   for states in dfa2_table:
      for idx, x in enumerate(dfa2_table[states]):
         for y in range(len(E)):
            dfa2_table[states][x] = transition_table2[states][idx]

   #Creating Complement Table for construction
   complement_table = OrderedDict()
   for i in range(total_States):
      complement_table[i] = OrderedDict()
      for x in E:
         complement_table[i][x] = ''
   # Looping through each one, theres definitely a better way but will just do this for now
   # for i in dfa_table:
   #    for j in dfa2_table:
   #       state = str(i)+str(j)
   #       for x in E: # Going through the alphabet
   #          S = dfa_table[i][x] + dfa2_table[j][x]
   #          complement_table[theStates.index(str(i) + str(j))][x] = theStates.index(S)

   ## Below was a Faster way
   print("Number of states:", total_States)
   print("Accepting states:", end= " ")
   for i in iOfAccept:
      print(i, end=" ")
   print()
   print(Alphabet)
   for i in dfa_table: ## Thought printing out each one as many times as alphabet length would be faster
      for j in dfa2_table:
         for idx, x in enumerate(E):
            S = theStates.index(dfa_table[i][x] +','+ dfa2_table[j][x])
            if(idx < len(E)):
               print(S, end=" ")
         print()

run_script()



