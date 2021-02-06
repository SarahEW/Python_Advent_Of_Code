# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:44:08 2020

@author: sarah
"""

import numpy as np
import itertools


rows = []
with open('input.txt') as f:
	for line in f:
		line=line.strip()
		row = list(line)
		#print(row)
		row = list(itertools.islice(itertools.cycle(row), 0,5000))
		rows.append(row)


stackedarray=np.stack(rows)
print(stackedarray)



patterns = [[[x,x*1] for x in range(0,323)],
			[[x,x*3] for x in range(0,323)],
			[[x,x*5] for x in range(0,323)],
			[[x,x*7] for x in range(0,323)],
			[[x*2,x] for x in range(0,323)]]

#pattern = [[x,x*3] for x in range(0,323)]
countlist = []

for pattern in patterns:
	treecount = 0
	for n,i in pattern:
		if n < 324:
			print(n,i)
			print(stackedarray[n][i])
			if stackedarray[n][i] == '#':
				treecount += 1
			
	print(treecount)
	countlist.append(treecount)

result = 1
for x in countlist:
	result = result * x 
	
print(result)
	