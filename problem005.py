#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#this one is easier on paper at this particluar level. The solution is to factor integers and add necessary factors.
#this solution could be made much more robust by building a factoring function and then comparing the list to the master list and appending as necessary

victory = False
count =2520

while not victory:
	if count % 19 == 0 and count % 17 == 0 and count % 16 == 0 and count % 14 == 0 and count % 13 == 0 and count % 12==0 and count % 11== 0:
		victory = True
		print count
	count += 2520


