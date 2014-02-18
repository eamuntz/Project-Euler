'''
#Starting with 1 and spiralling anticlockwise in the following way, 
#a square spiral with side length 7 is formed.

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

#It is interesting to note that the odd squares lie along the bottom right diagonal, 
#but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
#that is, a ratio of 8/13 approximates to 62%.

#If one complete new layer is wrapped around the spiral above, 
#a square spiral with side length 9 will be formed. If this process is continued, 
#what is the side length of the square spiral for which the ratio of primes along 
#both diagonals first falls below 10%?
'''

from prime import miller_rabin as is_prime
import time

#time code
start= time.time()


#---------

corners = 5.000000000000000000000
corner_primes = 0
side_length = 3

while True:
	#test all corners to see if they are primes
	#note the lower right diagnoal will never be prime since it is composed of odd squars
	a = side_length ** 2 - (side_length-1)
	b = a - (side_length - 1)
	c = b - (side_length - 1)
	
	if is_prime(a):
		corner_primes+=1

	
	if is_prime(b):
		corner_primes+=1


	if is_prime(c):
		corner_primes+=1
	
	#test to see if we meet the victory condition for problem (<10%)
	
	if corner_primes/corners<.100:
		print side_length
		print corner_primes/corners
		print 1000*(time.time()-start)
		break

	# adjust variables to continue to next layer
	side_length +=2
	corners+=4.00





