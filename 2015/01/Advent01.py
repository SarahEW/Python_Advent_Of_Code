# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:38:46 2020

@author: sarah
"""

import numpy as np

floor = 0
with open('input.txt') as data:
	array = [list(line) for line in data]
	for instruction in array[0]:
		print(instruction)
		if instruction == '(':
			floor = floor + 1
		elif instruction == ')':
			floor = floor - 1
	print(floor)
	

floor = 0
with open('input.txt') as data:
	array = [list(line) for line in data]
	for i, instruction in enumerate(array[0]):
		if floor == -1:
			print(floor)
			print(i)
			break
		elif instruction == '(':
			floor = floor + 1
		elif instruction == ')':
			floor = floor - 1
	#print(floor)
		