#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position 
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
from string import ascii_uppercase
f = open('problem022_names.txt')
names=f.readlines()
names=names[0].strip('"')
names=names.split('","')
names.sort()

alpha_dict=dict(zip(list(ascii_uppercase),range(1,27)))
total = 0
index=1

for each in names:
	sub=0	
	for char in each:
		sub+=alpha_dict[char]
	total+=sub*index
	index+=1
print total
