#prime generation
import math
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


# a = sieve(999999);

