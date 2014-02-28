'''
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import math

def factor_sum(number):
	total=1
	sqrt=math.sqrt(number)
	for each in range(2,int(math.ceil(sqrt))):
		if number%each==0:
			total+=each+(number/each)
	if int(sqrt)**2==number:
		total+=int(sqrt)
	return total

abundant=[]
for each in range(12,28101):
	if factor_sum(each)>each:
		abundant.append(each)

abu_sums=set()
a=abundant.pop(0)
while a<28124/2:
	abu_sums.add(a+a)
	for each in abundant:
		temp_sum=a+each
		if temp_sum<28124:			
			abu_sums.add(temp_sum)
		else:
			break

	a=abundant.pop(0)
finish=set.difference(set(range(28124)),abu_sums)	
print sum(finish)

