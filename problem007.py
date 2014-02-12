#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

#This is obviously a lazy implementation and could be improved by 
#adding a function to sieve that operates until a certain number of primes is achieved.

import sieve

primes = sieve.sieve(1000000)

print primes[10000]