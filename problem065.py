'''
Problem 065
The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

#my added notes
2/1,3/1,8/3, 11/4, 19/7, 87/32,106/39, 193/71,  1264/465, 10th
  1 ,1  , 2,  1     ,1   , 4   ,  1   ,   1,      6 , 

   n=k+(n-1)
   k= (n-2)+(n-1[with denominator *k])
   m= n+k
'''
import time
start=time.time()

def eCon(term):

	k = 4
	conCount = 6

	aNum=19
	aDem=7
	bNum=87
	bDem=32
	cNum=0
	cDem=0

	while conCount<term:
		
		conCount+=1

		if conCount % 3 == 0:
			k+=2
			cNum=aNum+bNum*k
			cDem=aDem+bDem*k
		else:
			cNum=aNum+bNum
			cDem=aDem+bDem

		aNum, aDem,bNum,bDem = bNum,bDem,cNum,cDem

	return bNum

n= eCon(100)


r = 0
while n:
	r, n = r + n % 10, n / 10
print r

print 1000*(time.time()-start)
