# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:01:01 2020

@author: sarah
"""

import numpy as np


data = np.loadtxt('input.txt')

ans = None


for a in data:
	for b in data:
		if a + b == 2020:
			print(a,b)
			ans = a * b
			break
	if ans:
		print(ans)
		break
		


for a in data:
	for b in data:
		for c in data:
			if a + b + c == 2020:
				print(a,b,c)
				ans2 = a * b * c
				break
		
print(ans2)
