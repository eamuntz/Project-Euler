#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the 
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
#I had a self written tool for this in java but given the repos use of python, I 
#just recoded this simple solution using the excellent module itertools

import itertools
f=list(itertools.permutations(range(10),10))
print ''.join(map(str,f[999999]))
