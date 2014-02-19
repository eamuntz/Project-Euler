'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

for a in range(1,1000):
	a2= a**2
	for b in range(1,1000):
		b2=b**2
		c = 1000-a-b
		c2=c**2
		if c2==a2+b2:
			print a*b*c
			break