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
TTable = []
TTable2 = []
theStates = []

def run_script():
   if(len(sys.argv) == 2):
      getComplement()
   elif(len(sys.argv) == 3):
      productConstruction()

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

def productConstruction():
   # Reading in files
   for line in open(sys.argv[1]):
      dfa1.append(line.replace('\n',''))
   for line in open(sys.argv[2]):
      dfa2.append(line.replace('\n',''))
   for x in dfa1[0]:
     if x.isdigit():
       tempList1.append(x)
   dfa1_Q = int(''.join(tempList1))
   for x in dfa2[0]:
     if x.isdigit():
       tempList2.append(x)
   
   #4/24
   tempInt = ''.join(tempList2)
   dfa2_Q = int(tempInt)

   dfa1_accept = re.findall('\d+',dfa1[1])
   dfa2_accept = re.findall('\d+',dfa2[1])

   #4/24
   total_States = int(((2 * dfa1_Q)/2) * dfa2_Q)

   #4/24
   #for i in range(dfa1_Q):
   #   for j in range(dfa2_Q):
   #      theStates.append(str(i) +','+ str(j))
   #accept_States = []
   az = 0
   for w in range(dfa1_Q):
	   for s in range(dfa2_Q):
		   theStates.append(str(w) +','+ str(s))
	   az += 1
   accept_States = []

   #for i in dfa1_accept:
   #   for j in dfa2_accept:
   #      accept_States.append(i +','+ j)
   #iOfAccept = []
   #for i in accept_States:
   #   iOfAccept.append(theStates.index(i))

   t = 0
   q = 0
   zz =0
   while t in dfa1_accept:
	   while q in dfa2_accept:
		   accept_States.append(t +','+ q)
		   q += 1
		   zz +=1
	   t +=1
	   zz+=1
   iOfAccept = []
   for i in accept_States:
      iOfAccept.append(theStates.index(i))

   alpha = dfa1[2]
   for x in dfa1[2][10:]:
	   E.append(x)
   ## DFA 1
   dfa_table = OrderedDict()

   for i in range(dfa1_Q):
      dfa_table[i] = OrderedDict()
      for x in E:
         dfa_table[i][x] = ''
   for x in dfa1[3:]:
	   TTable.append(x)

   k = 0
   while k < len(TTable):
	   TTable[k] = re.findall('\d+', TTable[k])
	   k += 1

   for states in dfa_table:
      for idx, x in enumerate(dfa_table[states]):
         for y in range(len(E)):
            dfa_table[states][x] = TTable[states][idx]

   # DFA 2
   dfa2_table = OrderedDict()
   for i in range(dfa2_Q):
      dfa2_table[i] = OrderedDict()
      for x in E:
         dfa2_table[i][x] = ''
   for x in dfa2[3:]:
	   TTable2.append(x)

   h = 0
   while h < len(TTable2):
	   TTable2[h] = re.findall('\d+', TTable2[h])
	   h += 1

   zzz = 0
   for states in dfa2_table:
	   for idx, x in enumerate(dfa2_table[states]):
		   for y in range(len(E)):
			   zzz += 1
		   dfa2_table[states][x] = TTable2[states][idx]
   complement_table = OrderedDict()
   for i in range(total_States):
	   complement_table[i] = OrderedDict()
	   for x in E:
		   complement_table[i][x] = ''

   print("Number of states:", total_States)
   print("Accepting states:", end= " ")
   for i in iOfAccept:
	   print(i, end=" ")
   print()
   print(alpha)
   for i in dfa_table:
	   for j in dfa2_table:
		   for idx, x in enumerate(E):
			   S = theStates.index(dfa_table[i][x] +','+ dfa2_table[j][x])
			   if(idx < len(E)):
				   print(S, end=" ")

print()
run_script()



