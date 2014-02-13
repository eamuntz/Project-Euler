
#It is possible to show that the square root of two can 
#be expressed as an infinite continued fraction.

#sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

#By expanding this for the first four iterations, we get:

#1 + 1/2 = 3/2 = 1.5
#1 + 1/(2 + 1/2) = 7/5 = 1.4
#1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

#The next three expansions are 99/70, 239/169, and 577/408, 
#but the eighth expansion, 1393/985, is the first example where 
#the number of digits in the numerator exceeds the number of digits in the denominator.

#In the first one-thousand expansions, how many fractions contain a numerator 
#with more digits than denominator?


from fractions import Fraction as F

def compare(fraction):
	if len(str(fraction.numerator))>len(str(fraction.denominator)):
		return True
	else:
		return False

oldn = 1
oldd = 1
n = 3
d = 2

count = 0

for i in range(1,1001):

	if compare(F(n,d)):
		count+=1

	newn = oldn+(2*n)
	newd = oldd+(2*d)
	oldn = n
	oldd = d
	n = newn
	d = newd


print count


'''
### This code ought to work but does not due to an stack overflow of nested functions
###
#function to compare numerator length and denominator length. If N>D return True

def compare(fraction):
	if len(str(fraction.numerator))>len(str(fraction.denominator)):
		return True
	else:
		return False

count = 0
squeeze='+Fraction(1,2)'
accordion ='Fraction(1)+Fraction(1,2)'

#problem asks for 1000 iterations. we begin on iteration 2
for i in range(2,1001):
	
	if compare(eval(accordion)):
		count+=1

	#modify the function  to include another 'layer
	splitQ = accordion.rfind('2')+1
	accordion = accordion[:splitQ]+squeeze+accordion[splitQ:]
	print count
	print i

print count

'''