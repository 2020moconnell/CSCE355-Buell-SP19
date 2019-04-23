# Maggie O'Connell
# CSCE 355 Buell
# 4/24/19
# 1: Inverse Homomorphism

import sys
import re
from collections import OrderedDict
tempList1 = []
DFAinfo = []
TTable = []
HTable
HOMinfo = []
input_E = []
Q = []
E = []
F = []
h_strings = []

def findInverse():
   dfa = OrderedDict()
   for line in open(sys.argv[1]):
     DFAinfo.append(line.replace('\n',''))

   # Getting # of States, Putting Accepting States and Alphabet into it's own LIST.
   for x in DFAinfo[0]:
     if x.isdigit():
       tempList1.append(x)
   Q = int(''.join(tempList1))

   for x in DFAinfo[1].split():
     if x.isdigit():
       F.append(int(x))

   for x in DFAinfo[2][10:]:
     E.append(x)

   #Putting in dict
   h = 0
   while h < Q:
     dfa[h] = OrderedDict()
     for x in E:
       dfa[h][x] = ''
     h += 1

   # Messing and converting for ease of access/traverse
   #TTable = [x for x in DFAinfo[3:]]
   for x in DFAinfo[3:]:
	   TTable.append(x)
   for i in range(len(TTable)):
      TTable[i] = re.findall('\d+', TTable[i])
   #Matching inputed transition to dict
   for states in dfa:
      for idx, x in enumerate(dfa[states]):
         for y in range(len(E)):
            dfa[states][x] = TTable[states][idx]

   #HOMinfo = [line.rstrip('\n') for line in open(sys.argv[2])]
   for line in open(sys.argv[2]):
     HOMinfo.append(line.replace('\n',''))

   #input_E = [x for x in HOMinfo[0][16:]]
   for x in HOMinfo[16:]:
	   inout_E.append(x)

   #Creating separate table for invhom
   #HTable = OrderedDict()
   #for i in range(Q):
   #   HTable[i] = OrderedDict()
   #   for x in input_E:
   #      HTable[i][x] = ''


   b = 0
   while b < Q:
     dfa[b] = OrderedDict()
     for x in E:
       dfa[b][x] = ''
     b += 1
   # Saving h(w).. to run through given DFA and get states to assign
   #h_strings = [x for x in HOMinfo[2:]]
   for x in HOMinfo[2:]:
	   h_strings.append(x)

   # Traversing through h(0), h(1), .... h(n) inside the DFA to match the state to the new homo table
   z = 0
   for idx, x in enumerate(input_E):
	   while z < Q:
		   S = z
		   for y in h_strings[idx]:
			   S = dfa[int(S)][y] # Traversing through DFA
		   HTable[i][x] = S # Found state so setting in new homo table
		   z += 1


   #for idx, x in enumerate(input_E):
   #   for i in range(Q):
   #      S = i
   #      for y in h_strings[idx]:
   #         S = dfa[int(S)][y] # Traversing through DFA
   #      HTable[i][x] = S # Found state so setting in new homo table

   print("Number of states:", Q)
   print(DFAinfo[1])
   print("Alphabet: ",end="")
   for x in input_E:
      print(x,end="")
   print()
   for x in HTable:
      for y in HTable[x]:
         print(HTable[x][y], end= " ")
      print()

findInverse()