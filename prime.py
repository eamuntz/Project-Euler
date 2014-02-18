import math
import random
#tools to help with questions involving prime numbers
#code from other sources is noted with url's leading to source


'''
http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing
pseudo-prime checks that should hold for numbers below

When the number n to be tested is small, trying all a < 2(ln n)2 is not necessary, as much smaller sets of potential witnesses are known to suffice. For example, Pomerance, Selfridge and Wagstaff[8] and Jaeschke[9] have verified that
if n < 1,373,653, it is enough to test a = 2 and 3;
if n < 9,080,191, it is enough to test a = 31 and 73;
if n < 4,759,123,141, it is enough to test a = 2, 7, and 61;
if n < 1,122,004,669,633, it is enough to test a = 2, 13, 23, and 1662803;
if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11;
if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13;
if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17.
'''


def miller_rabin(m, k = 3):
    s=1
    t = (m-1)/2
    while t%2 == 0:
        t /= 2
        s += 1

    for r in range(0,k):
    	rand_num = random.randint(1,m-1)
        y = pow(rand_num, t, m)
        prime = False

        if (y == 1):
            prime = True


        for i in range(0,s):
            if (y == m-1):
                prime = True
                break
            else:
                y = (y*y)%m

        if not prime:
            return False

    return True
  	
	




'''generate primes up to a limit using the Sieve of Eratosthenes (http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)'''

def sieve(limit):
	
	primes = []
	output = []
	upperLimit = int(math.sqrt(limit))

	for i in range(0,limit):
		primes.append(True)

	for i in range(2,upperLimit+1):
		if primes[i]:
			j = i * i
			while j<limit:
				primes[j] = False;
				j += i
			#for(var j = i*i; j<limit; j+=i):
			#	primes[j] = false;

	for i in range(2,limit):
		if(primes[i]==True):
			output.append(i)


	return output
