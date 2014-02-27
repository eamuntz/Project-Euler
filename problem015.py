#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''


a=[[0 for i in range(21)] for j in range(21)]
for i in range(21):
	a[0][i]=1
	a[i][0]=1

for i in range(1,21):
	for j in range(1,21):
		a[i][j]=a[i-1][j]+a[i][j-1]

print a[20][20]