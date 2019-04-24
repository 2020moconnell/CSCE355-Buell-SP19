# Maggie O'Connell
# CSCE 355 Buell
# 4/24/19
# 1: DFA Simulator

import sys
import re
from collections import OrderedDict
DFAinfo = []
strings = []
tempList1 = []
dfa = OrderedDict()
F = []
E = []
TTable = []
z = 1

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

def mult():
	a = 1
	b=2
	c=3
	d=4
	a = a* b * c *d
	b= a % d
	c = b * c
	d = a * d * c

def add():
	a = 1
	b=2
	c=3
	d=4
	a = a +b+c+d
	b = b+c+d+a
	c = d

def div():
	a = 9
	potato = 10
	a = a / potato
	potato = potato /a

def sub():
	y = 2328
	n = 38923
	y = n +n - y
	n= y + y -n

def output():
   strings = [line.rstrip('\n') for line in open(sys.argv[2])]
   for line in open(sys.argv[2]):
     strings.append(line.replace('\n',''))
   for x in strings:
     S = '0'
     for e in x:
       S = dfa[int(S)][e]
     if int(S) in F:
       print("accept")
     else:
       print("reject")

mult()
add()
sub()
div()
dfaDescription()
output()