# Maggie O'Connell
# CSCE 355 Buell
# 4/24/19
# 3: Inverse Homomorphism

import sys
import re
from collections import OrderedDict
tempList1 = []
DFAinfo = []
TTable = []
HOMinfo = []
input_E = []
Q = []
E = []
F = []
h_strings = []
z = 0

def findInverse():
   dfa = OrderedDict()
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

   h = 0
   while h < Q:
     dfa[h] = OrderedDict()
     for x in E:
       dfa[h][x] = ''
     h += 1

   for x in DFAinfo[3:]:
	   TTable.append(x)
   for i in range(len(TTable)):
      TTable[i] = re.findall('\d+', TTable[i])

   for states in dfa:
      for idx, x in enumerate(dfa[states]):
         for y in range(len(E)):
            dfa[states][x] = TTable[states][idx]

   for line in open(sys.argv[2]):
     HOMinfo.append(line.replace('\n',''))

   for x in HOMinfo[0][16:]:
	   input_E.append(x)

   homo_table = OrderedDict()
   for i in range(Q):
      homo_table[i] = OrderedDict()
      for x in input_E:
         homo_table[i][x] = ''

   for x in HOMinfo[2:]:
	   h_strings.append(x)

aa = 0
for idx, x in enumerate(input_E):
	while aa == 0:
		for i in range(Q):
			z +=1
		S = i
        for y in h_strings[idx]:
			S = dfa[int(S)][y]
			z +=1
        homo_table[i][x] = S
        aa += 1

print("Number of states:", Q)
print(DFAinfo[1])
print("Alphabet: ",end="")
for x in input_E:
	print(x,end="")
print()
for x in homo_table:
  for y in homo_table[x]:
	 print(homo_table[x][y], end= " ")
print()
      

findInverse()