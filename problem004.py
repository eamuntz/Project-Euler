#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
#Find the largest palindrome made from the product of two 3-digit numbers.

#easy improvement possible by reversing ranges and breaking once 'top values' when multiplied are less than  current answer value
#our answer is the LARGEST palindrome
answer = 0

for i in range(100,1000):
	for j in range(i,1000):
		if str(i*j)==str(i*j)[::-1] and i*j>answer:
			answer = i*j
print answer