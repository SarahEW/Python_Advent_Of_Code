# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:01:01 2020

@author: sarah
"""

import numpy as np

count = 0

with open('input.txt') as f:
	for line in f:
		criteria = line.split(':')[0]
		password = line.split(':')[1].strip()
		
		criterialetter = criteria.split(' ')[1]
		criteriarange = criteria.split(' ')[0].split('-')
		print(criteria, password)
		print(list(password).count(criterialetter))
		if int(criteriarange[0]) <= list(password).count(criterialetter) <= int(criteriarange[1]):
			 print('within criteria')
			 count += 1
 
print(count)

count = 0
with open('input.txt') as f:
	for line in f:
		criteria = line.split(':')[0]
		password = line.split(':')[1].strip()
		
		criterialetter = criteria.split(' ')[1]
		criterianumber = [int(x)-1 for x in criteria.split(' ')[0].split('-')]
		print(criteria, password)
		print(password[criterianumber[0]],password[criterianumber[1]])
		stack = np.stack((list(password),range(len(password))))
		print(stack)
		#print(criterialetter, password[criterianumber[0]],password[criterianumber[0]])
		if (password[criterianumber[0]] == criterialetter and password[criterianumber[1]] != criterialetter) or\
			(password[criterianumber[0]] != criterialetter and password[criterianumber[1]] == criterialetter):
			 
			 print('matches criteria')
			 count += 1
 
print(count)