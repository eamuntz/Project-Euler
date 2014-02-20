'''
Problem 20
Find the sum of the digits in the number 100!
'''
product = 1

for i in range(2,101):
	product*=i
	while product%10==0:
		product/=10

list_product=list(str(product))

sum_product=0

for each in list_product:
	sum_product+=int(each)

print sum_product