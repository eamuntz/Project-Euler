# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

#Program Note: I rewrote my initial solution to include a component necessary for later problems.
#Thus, though overkill for this problem, it was actually a smoother solution than transfering my original Java implementation.

import sieve
import math

target = 600851475143

possibleFactors = sieve.sieve(int(math.sqrt(target)))
while possibleFactors:
	i = possibleFactors.pop()
	if target % i == 0:
		print i
		break


