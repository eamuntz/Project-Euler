'''
Problem 12




'''

import prime
import math

primes = prime.sieve(10000)
not_found = True
triangle_num =3 
counter_num =3
while not_found:
	factored_num = triangle_num
	factor_counter = 1
	if not prime.miller_rabin(triangle_num):
		for i in primes:
			factor_pow=0
			while factored_num%i ==0:
				factor_pow+=1
				factored_num=factored_num/i
			factor_counter*=(factor_pow+1)
			if factored_num ==1 :
				break
		if factor_counter >500:
			print triangle_num
			not_found = False
	triangle_num+= counter_num
	counter_num+=1

