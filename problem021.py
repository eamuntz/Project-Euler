#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
'''
#definitely room for optimization in this solution. Specifically, improving factor_sum function
#and moving away from list iteration.

def factor_sum(number):
	factor_sum=1
	for i in range(2,number):
		if number%i==0:
			factor_sum+=i
	return factor_sum

amicable = 0

test = range(4,10001)

while test:
	a=test.pop()
	b=factor_sum(a)
	if factor_sum(b)==a and a!=b:
		test.remove(b)
		amicable+=a+b

print amicable