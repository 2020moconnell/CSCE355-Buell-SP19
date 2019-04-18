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
	
	