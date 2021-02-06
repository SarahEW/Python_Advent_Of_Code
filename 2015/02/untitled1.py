# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:19:26 2020

@author: sarah
"""

import numpy as np

total = 0
with open('data.txt') as data:
	for line in data:
		array = np.array([int(val) for val in line.split('x')])
		array = np.sort(array)
		l = int(array[0])
		w = int(array[1])
		h = int(array[2])
		print(l,w,h)
		ribbon = l+l+w+w
		bow = l*w*h
		total = total + ribbon + bow
		
print(total)
		