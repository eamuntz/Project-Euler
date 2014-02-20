'''
Problem 16
What is the sum of the digits of the number 2**1000
'''
a= 2**1000
b=[]
while a>0:
	b.append(a%10)
	a/=10
print sum(b)
