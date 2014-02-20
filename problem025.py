'''
Problem 25

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

def fibGen():
	a=1
	b=2
	c=0
	while True:
		c= a+b
		a,b=b,c
		yield b

fibGen=fibGen()
count = 4
while True:

	fib = fibGen.next()
	if len(str(fib))>999:
		print count
		break
	else:
		count+=1