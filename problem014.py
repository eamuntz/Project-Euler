

#works but this would easily be improved by implementing another funtion that tracks the counts along the way so that after two is reached, all values prior in the string can also be assigned values. 
max_chain, max_i = 0, 0
previous = [0,0]
for i in range(2,1000000):
	prev_len = len(previous)
	mutant = i
	counter = 0
	
	while mutant != 1:
		if mutant % 2 ==0:
			mutant=mutant/2
		else:
			mutant=3*mutant +1
		counter+=1
		if mutant<prev_len:
			counter+=previous[mutant]
			mutant = 1
	
	if counter > max_chain:
		max_chain = counter
		max_i = i

print max_i
print max_chain

