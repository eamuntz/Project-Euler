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
'''
def millerRabin(n, k = 7):
   """use Rabin-Miller algorithm to return True (n is probably prime)
      or False (n is definitely composite)"""
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1
      for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in xrange(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop
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
