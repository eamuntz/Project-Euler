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